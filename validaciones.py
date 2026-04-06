"""
MÓDULO DE VALIDACIONES (DEV 2 - David)
--------------------------------------
Este módulo contiene todas las reglas de calidad de datos del Ayuntamiento.
Proporciona funciones seguras que no rompen el programa si el usuario se equivoca.

Instrucciones para el equipo:
- DEV 1: Importa estas funciones en tu menu.py (ej: from validaciones import validar_temperatura)
- DEV 3: Usa validar_duplicado antes de guardar en tu archivo JSON.
"""

from datetime import datetime

def validar_temperatura():
    """
    Solicita y valida la temperatura.
    Rango permitido: -20 a 50 grados Celsius.
    
    DEV 1: Llama a esta función sin parámetros.
    Retorna: Un número float (ej. 25.5).
    """
    while True:
        try:
            entrada = input("Introduce la temperatura (-20 a 50 °C): ")
            temp = float(entrada)
            
            if -20 <= temp <= 50:
                return temp  
            else:
                print(f"❌ Error: {temp}°C está fuera del rango permitido (-20 a 50).")
        
        except ValueError:
            print("❌ Error: Por favor, introduce un número válido (ejemplo: 25.5).")
        
        print("🔄 Inténtalo de nuevo.\n")


def validar_humedad():
    """
    Solicita y valida la humedad ambiental.
    Rango permitido: 0 a 100%.
    
    DEV 1: Llama a esta función sin parámetros.
    Retorna: Un número float (ej. 45.0).
    """
    while True:
        try:
            entrada = input("Introduce la humedad (0 a 100%): ")
            humedad = float(entrada)
            
            if 0 <= humedad <= 100:
                return humedad  
            else:
                print(f"❌ Error: {humedad}% no es una humedad lógica (debe ser de 0 a 100).")
        
        except ValueError:
            print("❌ Error: Introduce un valor numérico para la humedad.")
            
        print("🔄 Inténtalo de nuevo.\n")


def validar_viento():
    """
    Solicita y valida la velocidad del viento.
    Rango permitido: 0 a 150 km/h.
    
    DEV 1: Llama a esta función sin parámetros.
    Retorna: Un número float (ej. 12.5).
    """
    while True:
        try:
            entrada = input("Introduce la velocidad del viento (0 a 150 km/h): ")
            viento = float(entrada)
            
            if 0 <= viento <= 150:
                return viento  
            else:
                print(f"❌ Error: {viento} km/h está fuera del rango lógico (0 a 150).")
        
        except ValueError:
            print("❌ Error: La velocidad del viento debe ser un valor numérico.")
            
        print("🔄 Inténtalo de nuevo.\n")


def validar_fecha():
    """
    Solicita y valida una fecha.
    Formato estricto: AAAA-MM-DD.
    
    DEV 1: Llama a esta función sin parámetros.
    Retorna: Un string con la fecha correcta (ej. '2026-04-06').
    """
    while True:
        entrada = input("Introduce la fecha (formato AAAA-MM-DD, ej: 2026-04-06): ").strip()
        
        if not entrada:
            print("❌ Error: La fecha no puede estar vacía.")
            continue 
            
        try:
            # Comprueba matemáticamente si la fecha existe en el calendario real
            datetime.strptime(entrada, "%Y-%m-%d")
            return entrada
            
        except ValueError:
            print("❌ Error: Formato incorrecto o fecha inexistente. Usa AAAA-MM-DD.")
            
        print("🔄 Inténtalo de nuevo.\n")


def validar_zona():
    """
    Solicita el nombre de la zona y verifica que no quede en blanco.
    
    DEV 1: Llama a esta función sin parámetros.
    Retorna: Un string con el nombre de la zona.
    """
    while True:
        zona = input("Introduce la zona (ej: Retiro, Centro): ").strip()
        if not zona:
            print("❌ Error: La zona no puede estar vacía.")
            print("🔄 Inténtalo de nuevo.\n")
        else:
            return zona


def validar_duplicado(nueva_fecha, nueva_zona, historial):
    """
    Comprueba si ya existe un registro para la misma fecha y zona.
    
    DEV 3 / DEV 1: Pasad a esta función la fecha, la zona y el JSON cargado.
    Retorna: True (si hay error de duplicado) o False (si todo está correcto).
    """
    for registro in historial:
        if registro['fecha'] == nueva_fecha and registro['zona'].lower() == nueva_zona.lower():
            print(f"❌ Error: Ya existen datos para '{nueva_zona}' en la fecha {nueva_fecha}.")
            print("⚠️ No se permiten registros duplicados para la misma zona el mismo día.")
            return True 
            
    return False