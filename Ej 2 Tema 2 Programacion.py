
palabra = input("Por favor, ingrese una palabra: ")
if len(palabra) < 2:
    print("La palabra debe contener al menos dos caracteres.")
else:
    palabra_intercambiada = palabra[-1] + palabra[1:-1] + palabra[0]
    print("Palabra con el primer y último carácter intercambiados:", palabra_intercambiada)
