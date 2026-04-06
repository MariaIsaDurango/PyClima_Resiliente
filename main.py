import sys
from datetime import datetime

def registrar_datos():
    print("\n--- 📝 REGISTRAR NUEVOS DATOS ---")
    try:
        # 1. Validación de Fecha
        fecha_input = input("Fecha (DD/MM/AAAA): ")
        fecha = datetime.strptime(fecha_input, "%d/%m/%Y").date()
        
        # 2. Distrito (Texto)
        distrito = str(input("Distrito de la ciudad: "))
        
        # 3. Temperatura (Decimales)
        temp = float(input("Temperatura (°C): "))
        
        # 4. Humedad (Decimales)
        humedad = float(input("Humedad (%): "))
        
        # 5. Viento (Entero)
        viento = int(input("Velocidad del viento (km/h): "))
        
        print(f"\n✅ Datos guardados para el distrito: {distrito}")
        print(f"Registro: {fecha} | Temp: {temp}°C | Viento: {viento}km/h")
        
    except ValueError as e:
        print(f"\n❌ ERROR DE FORMATO: Verifique los datos ingresados.")
        print(f"Detalle: {e}")

def main():
    while True:
        print("\n" + "="*30)
        print("   \U0001f324  SISTEMA PYCLIMA v1.1  ")
        print("="*30)
        print("1. Registrar Datos Climáticos")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            registrar_datos()
        elif opcion == "2":
            print("Cerrando sistema... ¡Buen día!")
            sys.exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()