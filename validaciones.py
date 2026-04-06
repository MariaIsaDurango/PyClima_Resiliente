"""
Módulo de Validaciones y Sistema de Alertas
DEV 4: Interfaz + Alertas
"""

import json
from datetime import datetime
from typing import Dict, List, Tuple

# ===== UMBRALES DE ALERTA =====
UMBRAL_TEMP_CALOR = 40.0  # °C
UMBRAL_VIENTO_ALTO = 50.0  # km/h
UMBRAL_HUMEDAD_BAJA = 20.0  # %
UMBRAL_HUMEDAD_ALTA = 95.0  # %


class SistemaAlertas:
    """
    Sistema integral de detección de riesgos climáticos.
    Analiza datos y genera alertas visuales llamativas.
    """
    
    def __init__(self):
        self.alertas_activas = []
        self.historial_alertas = []
    
    def analizar_datos(self, datos: Dict) -> Tuple[bool, List[str]]:
        """
        Analiza datos climáticos y detecta riesgos.
        
        Args:
            datos: Diccionario con temperatura, humedad, viento, lluvia, etc.
            
        Returns:
            Tupla (hay_alertas, lista_de_mensajes_alerta)
        """
        alertas = []
        
        # ALERTA 1: Calor extremo
        if "temperatura" in datos:
            alertas.extend(self._verificar_calor(datos["temperatura"]))
        
        # ALERTA 2: Viento peligroso
        if "viento" in datos:
            alertas.extend(self._verificar_viento(datos["viento"]))
        
        # ALERTA 3: Lluvia o humedad anómala
        if "lluvia" in datos or "humedad" in datos:
            alertas.extend(self._verificar_lluvia_humedad(
                datos.get("lluvia", False),
                datos.get("humedad", 50)
            ))
        
        self.alertas_activas = alertas
        return len(alertas) > 0, alertas
    
    def _verificar_calor(self, temperatura: float) -> List[str]:
        """Verifica si la temperatura supera umbrales críticos."""
        alertas = []
        
        if temperatura > 45:
            alertas.append(
                "\n" + "🔴" * 40 +
                "\n⚠️  ALERTA CRÍTICA: CALOR EXTREMO ⚠️" +
                f"\n   Temperatura: {temperatura}°C (NIVEL CRÍTICO)" +
                "\n   ACCIÓN INMEDIATA: Activar protocolo de emergencia." +
                "\n   - Cerrar espacios públicos si es necesario." +
                "\n   - Avisar a servicios de emergencia." +
                "\n   - Elevar nivel de vigilancia." +
                "\n" + "🔴" * 40
            )
        elif temperatura > UMBRAL_TEMP_CALOR:
            alertas.append(
                "\n" + "🟠" * 40 +
                "\n⚠️  ALERTA POR CALOR ⚠️" +
                f"\n   Temperatura: {temperatura}°C" +
                "\n   Riesgo: Golpes de calor, riesgo para población vulnerable." +
                "\n   Recomendación: Aumentar vigilancia en parques y zonas públicas." +
                "\n" + "🟠" * 40
            )
        
        return alertas
    
    def _verificar_viento(self, velocidad_viento: float) -> List[str]:
        """Verifica si el viento es peligroso."""
        alertas = []
        
        if velocidad_viento > 70:
            alertas.append(
                "\n" + "🔴" * 40 +
                "\n⚠️  ALERTA CRÍTICA: VIENTO EXTREMO ⚠️" +
                f"\n   Velocidad: {velocidad_viento} km/h (NIVEL CRÍTICO)" +
                "\n   ACCIÓN INMEDIATA:" +
                "\n   - Cerrar zonas afectadas." +
                "\n   - Alertar a ciudadanía." +
                "\n" + "🔴" * 40
            )
        elif velocidad_viento > UMBRAL_VIENTO_ALTO:
            alertas.append(
                "\n" + "🟠" * 40 +
                "\n⚠️  ALERTA POR VIENTO FUERTE ⚠️" +
                f"\n   Velocidad: {velocidad_viento} km/h" +
                "\n   Riesgo: Daños estructurales, riesgo de caídas de objetos." +
                "\n   Recomendación: Reforzar vigilancia, evitar actividades al aire libre." +
                "\n" + "🟠" * 40
            )
        
        return alertas
    
    def _verificar_lluvia_humedad(self, lluvia: bool, humedad: float) -> List[str]:
        """Verifica condiciones anómalas de lluvia y humedad."""
        alertas = []
        
        if lluvia or humedad > UMBRAL_HUMEDAD_ALTA:
            alertas.append(
                "\n" + "🟡" * 40 +
                "\n⚠️  ALERTA POR LLUVIA/HUMEDAD ⚠️" +
                f"\n   Estado: {'Lluvia activa' if lluvia else f'Humedad: {humedad}%'}" +
                "\n   Riesgo: Inundaciones, deslizamientos de tierra." +
                "\n   Recomendación: Monitorear zonas bajas y sistemas de drenaje." +
                "\n" + "🟡" * 40
            )
        elif humedad < UMBRAL_HUMEDAD_BAJA:
            alertas.append(
                "\n" + "🟡" * 40 +
                "\n⚠️  ALERTA POR SEQUEDAD EXTREMA ⚠️" +
                f"\n   Humedad: {humedad}%" +
                "\n   Riesgo: Falta de agua, sequedad extrema." +
                "\n   Recomendación: Implementar medidas de conservación de agua." +
                "\n" + "🟡" * 40
            )
        
        return alertas
    
    def mostrar_alertas_visuales(self) -> None:
        """Imprime todas las alertas de forma visual y llamativa."""
        if not self.alertas_activas:
            print("✅ No hay alertas activas. Condiciones normales.")
            return
        
        print("\n" + "=" * 80)
        print("           📋 RESUMEN DE ALERTAS DEL SISTEMA")
        print("=" * 80)
        
        for i, alerta in enumerate(self.alertas_activas, 1):
            print(f"\n[ALERTA {i}]")
            print(alerta)
        
        print("\n" + "=" * 80 + "\n")


def validar_input_numerico(prompt: str, tipo: type = float, rango: Tuple[float, float] = None) -> float | int:
    """
    Captura input numérico con validación y manejo de errores.
    
    Args:
        prompt: Mensaje a mostrar al usuario
        tipo: Tipo de dato esperado (float o int)
        rango: Tupla (min, max) para validar rango
        
    Returns:
        Valor numérico validado
    """
    while True:
        try:
            valor = tipo(input(prompt))
            
            if rango and (valor < rango[0] or valor > rango[1]):
                print(f"❌ ERROR: El valor debe estar entre {rango[0]} y {rango[1]}.")
                continue
            
            return valor
        
        except ValueError:
            tipo_nombre = "número" if tipo == float else "número entero"
            print(f"❌ ERROR: Debe ingresar un {tipo_nombre} válido.")
        except Exception as e:
            print(f"❌ ERROR inesperado: {e}")


def validar_input_si_no(prompt: str) -> bool:
    """
    Captura confirmación Sí/No del usuario.
    
    Args:
        prompt: Mensaje a mostrar
        
    Returns:
        True si el usuario ingresa 's' o 'si', False si ingresa 'n' o 'no'
    """
    while True:
        respuesta = input(prompt).strip().lower()
        
        if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no', 'nope']:
            return False
        else:
            print("❌ ERROR: Por favor, responda con 'S' (sí) o 'N' (no).")


def validar_zona(zona: str, zona_valida: bool = True) -> str:
    """
    Valida que la zona sea válida.
    
    Args:
        zona: Nombre de la zona ingresada
        zona_valida: Si se debe validar contra lista oficial
        
    Returns:
        Zona validada y formateada
    """
    zona_limpia = zona.strip().title()
    
    if not zona_limpia:
        raise ValueError("La zona no puede estar vacía.")
    
    return zona_limpia


def mostrar_resumen_registro(registro: Dict) -> None:
    """Muestra un resumen formateado del registro a guardar."""
    print("\n" + "=" * 60)
    print("           📊 RESUMEN DEL REGISTRO A GUARDAR")
    print("=" * 60)
    print(f"Fecha:        {registro.get('fecha', 'N/A')}")
    print(f"Zona:         {registro.get('distrito', 'N/A')}")
    print(f"Temperatura:  {registro.get('temperatura', 'N/A')}°C")
    print(f"Humedad:      {registro.get('humedad', 'N/A')}%")
    
    if 'viento' in registro:
        print(f"Viento:       {registro.get('viento', 'N/A')} km/h")
    if 'lluvia' in registro:
        print(f"Lluvia:       {'Sí' if registro.get('lluvia') else 'No'}")
    
    print("=" * 60 + "\n")
