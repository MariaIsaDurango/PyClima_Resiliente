"""
Script simple de validación - sin interacción
"""

from validaciones import SistemaAlertas

# Test rápido
sistema = SistemaAlertas()
datos_test = {
    "temperatura": 42,
    "viento": 55,
    "humedad": 96,
    "lluvia": True
}

hay_alertas, mensajes = sistema.analizar_datos(datos_test)
print("✅ Sistema de alertas inicializado correctamente.")
print(f"Datos de prueba: {datos_test}")
print(f"Alertas detectadas: {hay_alertas}")
print(f"Número de alertas: {len(mensajes)}")
print("\nMostrando alertas:")
sistema.mostrar_alertas_visuales()
