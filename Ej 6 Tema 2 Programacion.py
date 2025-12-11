# Solicitar al usuario qué desea calcular
opcion = input("¿Qué desea calcular? (densidad/masa/volumen): ").lower()

# Verificar la opción seleccionada y realizar el cálculo correspondiente
if opcion == "densidad":
    # Calcular la densidad
    masa = float(input("Ingrese la masa (en gramos): "))
    volumen = float(input("Ingrese el volumen (en cm³): "))
    densidad = masa / volumen
    print(f"La densidad es:",densidad,"g/cm³")

elif opcion == "masa":
    # Calcular la masa
    densidad = float(input("Ingrese la densidad (en g/cm³): "))
    volumen = float(input("Ingrese el volumen (en cm³): "))
    masa = densidad * volumen
    print(f"La masa es:",masa,"gramos")

elif opcion == "volumen":
    # Calcular el volumen
    masa = float(input("Ingrese la masa (en gramos): "))
    densidad = float(input("Ingrese la densidad (en g/cm³): "))
    volumen = masa / densidad
    print("El volumen es:",volumen," cm³")

else:
    print("Opción no válida. Por favor, elija 'densidad', 'masa' o 'volumen'.")

