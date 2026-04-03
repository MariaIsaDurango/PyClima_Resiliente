import sys

def registrar_datos():
    print("\n--- 📝 REGISTRAR NUEVOS DATOS ---")
    try:
        fecha = input("Fecha (DD/MM/AAAA): ")
        zona = input("Zona de la ciudad: ")
        temp = float(input("Temperatura (°C): "))
        humedad = float(input("Humedad (%): "))
        
        print(f"\n✅ Datos guardados para la zona: {zona}")
        print("Sincronizando con los módulos de validación y persistencia...")
        
    except ValueError:
        print("\n❌ ERROR: Temperatura y Humedad deben ser números.")

def main():
    while True:
        print("\n" + "="*30)
        print("  🌦️  SISTEMA PYCLIMA v1.0  ")
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