"""
Script de prueba para validar el sistema de alertas.
DEV 4: Pruebas de Alertas
"""

from validaciones import SistemaAlertas
import json

def test_alerta_calor():
    """Prueba las alertas por calor extremo."""
    print("\n" + "="*70)
    print("TEST 1: ALERTA POR CALOR")
    print("="*70)
    
    sistema = SistemaAlertas()
    
    # Caso 1: Calor crítico (> 45°C)
    print("\n[Caso 1] Temperatura crítica: 47°C")
    datos1 = {"temperatura": 47}
    hay_alertas, msg = sistema.analizar_datos(datos1)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema.mostrar_alertas_visuales()
    
    # Caso 2: Calor alto (40-45°C)
    print("\n[Caso 2] Temperatura alta: 42°C")
    sistema2 = SistemaAlertas()
    datos2 = {"temperatura": 42}
    hay_alertas, msg = sistema2.analizar_datos(datos2)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema2.mostrar_alertas_visuales()
    
    # Caso 3: Temperatura normal
    print("\n[Caso 3] Temperatura normal: 25°C")
    sistema3 = SistemaAlertas()
    datos3 = {"temperatura": 25}
    hay_alertas, msg = sistema3.analizar_datos(datos3)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema3.mostrar_alertas_visuales()


def test_alerta_viento():
    """Prueba las alertas por viento."""
    print("\n" + "="*70)
    print("TEST 2: ALERTA POR VIENTO")
    print("="*70)
    
    # Caso 1: Viento crítico (> 70 km/h)
    print("\n[Caso 1] Viento crítico: 80 km/h")
    sistema = SistemaAlertas()
    datos1 = {"viento": 80}
    hay_alertas, msg = sistema.analizar_datos(datos1)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema.mostrar_alertas_visuales()
    
    # Caso 2: Viento fuerte (50-70 km/h)
    print("\n[Caso 2] Viento fuerte: 60 km/h")
    sistema2 = SistemaAlertas()
    datos2 = {"viento": 60}
    hay_alertas, msg = sistema2.analizar_datos(datos2)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema2.mostrar_alertas_visuales()
    
    # Caso 3: Viento normal
    print("\n[Caso 3] Viento normal: 15 km/h")
    sistema3 = SistemaAlertas()
    datos3 = {"viento": 15}
    hay_alertas, msg = sistema3.analizar_datos(datos3)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema3.mostrar_alertas_visuales()


def test_alerta_lluvia():
    """Prueba las alertas por lluvia/humedad."""
    print("\n" + "="*70)
    print("TEST 3: ALERTA POR LLUVIA/HUMEDAD")
    print("="*70)
    
    # Caso 1: Lluvia activa
    print("\n[Caso 1] Lluvia activa")
    sistema = SistemaAlertas()
    datos1 = {"lluvia": True}
    hay_alertas, msg = sistema.analizar_datos(datos1)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema.mostrar_alertas_visuales()
    
    # Caso 2: Humedad alta
    print("\n[Caso 2] Humedad muy alta: 97%")
    sistema2 = SistemaAlertas()
    datos2 = {"humedad": 97}
    hay_alertas, msg = sistema2.analizar_datos(datos2)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema2.mostrar_alertas_visuales()
    
    # Caso 3: Humedad baja
    print("\n[Caso 3] Humedad muy baja: 18%")
    sistema3 = SistemaAlertas()
    datos3 = {"humedad": 18}
    hay_alertas, msg = sistema3.analizar_datos(datos3)
    print(f"¿Hay alertas?: {hay_alertas}")
    sistema3.mostrar_alertas_visuales()


def test_escenario_completo():
    """Prueba un escenario completo con múltiples parámetros."""
    print("\n" + "="*70)
    print("TEST 4: ESCENARIO COMPLETO CON MÚLTIPLES ALERTAS")
    print("="*70)
    
    print("\n[Caso: Tormenta con calor]")
    print("Datos: Temp 43°C, Humedad 96%, Viento 65 km/h, Lluvia Sí")
    
    sistema = SistemaAlertas()
    datos = {
        "temperatura": 43,
        "humedad": 96,
        "viento": 65,
        "lluvia": True
    }
    
    hay_alertas, msg = sistema.analizar_datos(datos)
    print(f"\n¿Hay alertas?: {hay_alertas}")
    print(f"Número de alertas: {len(msg)}")
    sistema.mostrar_alertas_visuales()


def main():
    """Ejecuta todos los tests."""
    print("\n" + "█"*70)
    print("  SUITE DE PRUEBAS: SISTEMA DE ALERTAS PYCLIMA RESILIENTE")
    print("█"*70)
    
    try:
        test_alerta_calor()
        input("\n\n[Presione ENTER para continuar con el siguiente test]")
        
        test_alerta_viento()
        input("\n\n[Presione ENTER para continuar con el siguiente test]")
        
        test_alerta_lluvia()
        input("\n\n[Presione ENTER para continuar con el siguiente test]")
        
        test_escenario_completo()
        
        print("\n" + "█"*70)
        print("  ✅ TODOS LOS TESTS COMPLETADOS SATISFACTORIAMENTE")
        print("█"*70 + "\n")
    
    except Exception as e:
        print(f"\n❌ ERROR EN LOS TESTS: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
