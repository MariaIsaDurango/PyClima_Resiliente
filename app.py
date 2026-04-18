import streamlit as st
import auth
import persistencia
import validaciones
import alertas
import analitica
from datetime import datetime
from interfaz import InterfazPyClima
import pandas as pd # Útil para mostrar los JSON de forma limpia

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="PyClima Resiliente v1.0", page_icon="🌦️", layout="wide")

# --- ESTADO DE SESIÓN ---
if 'usuario_autenticado' not in st.session_state:
    st.session_state.usuario_autenticado = None
if 'app_logic' not in st.session_state:
    st.session_state.app_logic = None

persistencia.inicializar_archivo_datos()

# --- FUNCIONES DE APOYO ---
def login_usuario(usuario, password):
    usuarios = auth.cargar_datos(auth.ARCHIVO_USUARIOS)
    user_found = None
    for u in usuarios:
        if str(u.get("num_empleado")) == str(usuario) and u.get("password") == password:
            user_found = u
            break
    
    if user_found:
        st.session_state.usuario_autenticado = user_found
        st.session_state.app_logic = InterfazPyClima(usuario_actual=user_found)
        st.success(f"✅ Acceso concedido.")
        st.rerun()
    else:
        st.error("❌ Credenciales incorrectas.")

def registrar_nuevo_usuario_streamlit(nombre, apellidos, num_empleado, password):
    usuarios = auth.cargar_datos(auth.ARCHIVO_USUARIOS)
    if any(str(u.get("num_empleado")) == str(num_empleado) for u in usuarios):
        return False, "⚠️ Este número de empleado ya existe."
    
    nuevo_u = {"nombre": nombre, "apellidos": apellidos, "num_empleado": num_empleado, "password": password}
    usuarios.append(nuevo_u)
    auth.guardar_datos(auth.ARCHIVO_USUARIOS, usuarios)
    return True, "✅ Registro exitoso."

# --- INTERFAZ DE LOGIN ---
if st.session_state.usuario_autenticado is None:
    st.title("🌦️ Sistema PyClima Resiliente")
    tab1, tab2 = st.tabs(["🔐 Iniciar Sesión", "📝 Registrar Nuevo Usuario"])

    with tab1:
        with st.form("login_form"):
            user_input = st.text_input("Número de Empleado")
            pass_input = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Entrar"):
                login_usuario(user_input, pass_input)

    with tab2:
        with st.form("register_form"):
            new_nombre = st.text_input("Nombre")
            new_apellido = st.text_input("Apellidos")
            new_id = st.text_input("Número de Empleado")
            new_pass = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Crear Cuenta"):
                exito, msj = registrar_nuevo_usuario_streamlit(new_nombre, new_apellido, new_id, new_pass)
                if exito: st.success(msj)
                else: st.warning(msj)

# --- PANEL PRINCIPAL ---
else:
    st.sidebar.title(f"👤 {st.session_state.usuario_autenticado.get('nombre')}")
    menu = st.sidebar.radio(
        "Navegación",
        ["Registrar Datos", "Consultar Datos (por zonas)", "Ver Histórico (todas las zonas)", "Alertas Activas", "Salir"]
    )
    
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.usuario_autenticado = None
        st.rerun()

    # --- LÓGICA DE LAS SECCIONES ---
    
    if menu == "Registrar Datos":
        st.title("📝 Registro de Datos")
        with st.form("registro_clima"):
            distritos = persistencia.obtener_distritos_permitidos()
            col1, col2 = st.columns(2)
            with col1:
                fecha = st.date_input("Fecha del Registro")
                distrito = st.selectbox("Zona/Distrito", distritos)
                temp = st.number_input("Temperatura (°C)", min_value=-20.0, max_value=50.0, value=20.0)
            with col2:
                humedad = st.slider("Humedad (%)", 0, 100, 50)
                viento = st.number_input("Viento (km/h)", min_value=0.0, value=10.0)
                lluvia = st.number_input("Precipitaciones (mm)", min_value=0.0, value=0.0)
            
            if st.form_submit_button("Guardar Registro"):
                nuevo_reg = {
                    "fecha": str(fecha), "distrito": distrito, "temp": temp, "temperatura": temp,
                    "humedad": humedad, "viento": viento, "lluvia": lluvia,
                    "registrado_por": st.session_state.usuario_autenticado["num_empleado"], "editado": False
                }
                if persistencia.registrar_nuevo_dato(nuevo_reg):
                    st.success("✅ Registro guardado correctamente.")
                else:
                    st.error("❌ Error al guardar. Posible duplicado.")

    elif menu == "Consultar Datos (por zonas)": 
        st.title("📊 Panel de Consultas y Filtros")
        datos = st.session_state.app_logic._cargar_datos()
        
        if not datos:
            st.warning("❌ No hay datos registrados.")
        else:
            df = pd.DataFrame(datos)
            tipo_filtro = st.radio("Método de búsqueda:", ["📍 Por Zona/Distrito", "📅 Por Fecha", "👤 Mis Registros"], horizontal=True)
            st.divider()

            if tipo_filtro == "📍 Por Zona/Distrito":
                distrito_sel = st.selectbox("Seleccione el Distrito:", sorted(df['distrito'].unique()))
                df_filtrado = df[df['distrito'] == distrito_sel]
            elif tipo_filtro == "📅 Por Fecha":
                fecha_sel = st.date_input("Seleccione la Fecha:")
                df_filtrado = df[df['fecha'] == str(fecha_sel)]
            else:
                mi_id = st.session_state.usuario_autenticado.get("num_empleado")
                df_filtrado = df[df['registrado_por'] == mi_id]

            if not df_filtrado.empty:
                st.dataframe(df_filtrado, use_container_width=True)
            else:
                st.error("🏠 No se encontraron registros.")

    elif menu == "Ver Histórico (todas las zonas)":
        st.title("📚 Historial Climático")
        datos = st.session_state.app_logic._cargar_datos()
        if datos:
            df = pd.DataFrame(datos)
            filtro = st.multiselect("Filtrar por distrito", df['distrito'].unique())
            if filtro:
                df = df[df['distrito'].isin(filtro)]
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No hay datos disponibles.")

    elif menu == "Alertas Activas":
        st.title("🚨 Panel de Alertas")
        datos = st.session_state.app_logic._cargar_datos()
        alertas_encontradas = False
        for reg in datos:
            alertas_locales = st.session_state.app_logic._analizar_alertas(
                reg.get('temp', 0), reg.get('humedad', 0), reg.get('viento', 0), reg.get('lluvia', 0)
            )
            if alertas_locales:
                alertas_encontradas = True
                with st.expander(f"⚠️ {reg['distrito']} - {reg['fecha']}"):
                    for a in alertas_locales: st.write(f"- {a}")
        if not alertas_encontradas: st.success("No hay alertas activas.")
        
    elif menu == "Salir":
        st.session_state.usuario_autenticado = None
        st.info("Sesión cerrada. ¡Hasta pronto!")
        st.rerun()