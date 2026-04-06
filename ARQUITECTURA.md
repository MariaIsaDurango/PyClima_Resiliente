# ARQUITECTURA DEL SISTEMA - PyClima Resiliente DEV 4

## 🏗️ DIAGRAMA DE COMPONENTES

```
┌─────────────────────────────────────────────────────────────────┐
│                    PYCLIMA RESILIENTE v1.0                      │
│              Sistema de Monitoreo Climático Avanzado             │
└─────────────────────────────────────────────────────────────────┘

                            ┌──────────────┐
                            │   main.py    │ ← PUNTO DE ENTRADA
                            │ InterfazUI   │
                            └──────┬───────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
        ┌──────▼─────────┐  ┌─────▼──────────┐  ┌───▼──────────────┐
        │    Menú        │  │  Registro      │  │  Consulta Zone   │
        │  Principal     │  │  + Análisis    │  │  + Histórico     │
        └────────────────┘  └────────┬───────┘  └──────────────────┘
                                     │
                            ┌────────▼────────┐
                            │ validaciones.py │ ◄ SISTEMA DE ALERTAS
                            │ SistemaAlertas  │
                            └────────┬────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
            ┌───────▼─────┐  ┌──────▼──────┐  ┌─────▼──────────┐
            │ Alerta      │  │ Alerta      │  │ Alerta Lluvia  │
            │ Calor       │  │ Viento      │  │ & Humedad      │
            └─────────────┘  └─────────────┘  └────────────────┘
                                     │
                            ┌────────▼─────────┐
                            │ persistencia.py  │ ◄ PERSISTENCIA
                            │ Registro JSON    │
                            └──────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
            ┌───────▼────────┐ ┌────▼──────────┐ ┌──▼──────────────┐
            │ config.json    │ │datos_clima   │ │Distritos Madrid │
            │(Distritos)     │ │.json (BD)    │ │(21 zonas)       │
            └────────────────┘ └──────────────┘ └─────────────────┘
```

## 📦 MÓDULOS Y RESPONSABILIDADES

### 1. **main.py** - Interfaz de Usuario (DEV 4)
```
Responsabilidades:
├── Menú Principal (5 opciones)
├── Captura de inputs numéricos
├── Captura de confirmaciones
├── Flujo de registro completo
├── Visualización de datos
├── Gestión de excepciones
└── Experiencia del usuario
```

**Características:**
- ✅ Menú interactivo sin crashes
- ✅ Validación de inputs con rangos
- ✅ Manejo completo de errores
- ✅ Confirmaciones antes de guardar
- ✅ Integración con alertas automáticas

### 2. **validaciones.py** - Sistema de Alertas (DEV 4)
```
Responsabilidades:
├── Clase SistemaAlertas
├── Análisis de 3 tipos de riesgo
├── Generación de mensajes visuales
├── Funciones de validación
├── Umbrales configurables
└── Sistema de puntuación de riesgo
```

**Detección de Riesgos:**
- 🔴 Calor Extremo (2 niveles)
- 🔴 Viento Peligroso (2 niveles)
- 🟡 Lluvia/Humedad Anómala (3 variantes)

### 3. **persistencia.py** - Gestión de JSON (DEV 3)
```
Responsabilidades (ya implementadas):
├── Lectura/escritura JSON
├── Validación de duplicados
├── Carga de configuración
└── Manejo de errores críticos
```

### 4. **config.json** - Configuración
```json
{
    "distritos_oficiales": [
        21 distritos de Madrid
    ]
}
```

### 5. **datos_clima.json** - Base de Datos
```
Formato de cada registro:
{
    "fecha": "DD/MM/AAAA",
    "distrito": "Nombre",
    "temperatura": float,
    "humedad": float,
    "viento": float,
    "lluvia": boolean,
    "timestamp": "ISO"
}
```

## 🔄 FLUJOS DE DATOS

### FLUJO 1: Registrar Datos + Alertas

```
Usuario selecciona "1"
    ↓
Input: Fecha (validada)
    ↓
Input: Zona (validada contra config.json)
    ↓
Input: Temperatura (validada -50 a 60)
    ↓
Input: Humedad (validada 0 a 100)
    ↓
Input: Viento (validada 0 a 200)
    ↓
Input: Lluvia (S/N)
    ↓
Mostrar Resumen
    ↓
SistemaAlertas.analizar_datos() ◄ ANÁLISIS AUTOMÁTICO
    ↓
¿Hay Alertas? ─→ Mostrar alertas visuales
               ├→ Preguntar si continuar
               └→ Si no: Cancelar
    ↓
Confirmación de guardado
    ↓
persistencia.registrar_nuevo_dato()
    ↓
Validar duplicados
    ↓
Guardar en JSON
    ↓
Confirmar al usuario: ✅ Guardado exitosamente
```

### FLUJO 2: Consultar por Zona

```
Usuario selecciona "2"
    ↓
Mostrar lista de 21 distritos
    ↓
Input: Nombre del distrito
    ↓
persistencia.leer_historico()
    ↓
Filtrar por distrito
    ↓
¿Registros encontrados? 
├→ SÍ: Mostrar lista con detalles
└→ NO: Mostrar mensaje y volver
    ↓
Total de registros
```

### FLUJO 3: Ver Histórico

```
Usuario selecciona "3"
    ↓
persistencia.leer_historico()
    ↓
¿Hay registros?
├→ SÍ: Mostrar todos ordenados
└→ NO: Mostrar mensaje vacío
    ↓
Total de registros acumulados
```

## ⚠️ SISTEMA DE ALERTAS - DETALLES

### Estructura de Análisis

```
analizar_datos(registro) → (hay_alertas, lista_mensajes)
    │
    ├─→ _verificar_calor(temperatura)
    │   ├─→ T > 45°C     → Alerta CRÍTICA
    │   ├─→ T > 40°C     → Alerta ALTA
    │   └─→ T ≤ 40°C     → Sin alerta
    │
    ├─→ _verificar_viento(velocidad)
    │   ├─→ V > 70 km/h  → Alerta CRÍTICA
    │   ├─→ V > 50 km/h  → Alerta ALTA
    │   └─→ V ≤ 50 km/h  → Sin alerta
    │
    └─→ _verificar_lluvia_humedad(lluvia, humedad)
        ├─→ Lluvia = true        → Alerta
        ├─→ H > 95%              → Alerta
        ├─→ H < 20%              → Alerta
        └─→ Condiciones normales  → Sin alerta
```

### Formato de Mensaje de Alerta

```
████████████████████████
⚠️  ALERTA [TIPO]
   [Parámetro]: [Valor] [Unidad]
   Riesgo: [Descripción]
   Recomendación: [Acción]
████████████████████████
```

## 🛡️ MECANISMOS DE SEGURIDAD Y VALIDACIÓN

### 1. Validación de Inputs
```
✓ Rango numérico
✓ Tipo de dato correcto
✓ Formato de fecha
✓ Confirmaciones S/N
✓ Sin inputs vacíos
```

### 2. Prevención de Errores
```
✓ Try-except en todas las funciones
✓ Reintentos sin límite
✓ Nunca cierra el programa por error
✓ Mensajes claros de error
✓ Confirmación antes de guardar
```

### 3. Integridad de Datos
```
✓ Validación de distrito contra config.json
✓ Prevención de duplicados por fecha+distrito
✓ Timestamp automático en cada registro
✓ Formato JSON validado
```

## 📊 ESTADÍSTICAS

| Componente | Líneas de Código | Funciones | Clases |
|-----------|-----------------|-----------|--------|
| main.py | 345 | 12 | 1 |
| validaciones.py | 350 | 8 | 1 |
| persistencia.py | 65 | 4 | 0 |
| **TOTAL** | **760** | **24** | **2** |

## 🧪 PRUEBAS

### Test Incluidos
- ✅ Alerta por Calor (Crítica y Alta)
- ✅ Alerta por Viento (Crítica y Alta)
- ✅ Alerta por Lluvia/Humedad (3 casos)
- ✅ Escenarios con múltiples alertas
- ✅ Validación de inputs
- ✅ Compilación sin errores

### Evidencia de Funcionamiento
```
Sistema de alertas: ✅ FUNCIONA
- Detectó 3 alertas con datos de prueba
- Análisis de: Temperatura 42°C, Viento 55 km/h, Humedad 96%
```

## 🚀 EJECUCIÓN

### Iniciar Sistema
```bash
# Activar entorno
.\.venv\Scripts\Activate.ps1

# Ejecutar aplicación
python main.py
```

### Ejecución de Tests
```bash
# Test simple
python test_simple.py

# Suite completa
python test_alertas.py
```

## 📋 CHECKLIST DE CUMPLIMIENTO

### Requerimientos DEV 4 ✅

- ✅ Menú Principal con opciones claras
- ✅ Inputs validados sin crashes
- ✅ Mensajes de error comprensibles
- ✅ Confirmación antes de guardar
- ✅ Alerta por Calor (>40°C)
- ✅ Alerta por Viento (>50 km/h)
- ✅ Mínimo 3 situaciones de riesgo detectadas
- ✅ Consulta de datos por zona
- ✅ Histórico de registros
- ✅ Integración con persistencia.py
- ✅ Testing funcional
- ✅ Interfaz UX amigable
- ✅ Robustez: No hay modo de romper el programa

---

**Desarrollador**: DEV 4 (Interfaz + Alertas)  
**Fecha**: 3 de Abril de 2026  
**Estado**: ✅ COMPLETO Y LISTO PARA INTEGRACIÓN
