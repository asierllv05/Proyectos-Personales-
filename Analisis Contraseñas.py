def cont(n):
    if len(n) < 8:
        if n.isdigit():
            print('Contraseña muy débil')
        elif n.isalpha():
            print('Contraseña débil')
        else:
            print('Contraseña Normal')
    elif len(n) >= 8:
        # Agregar lógica para determinar si la contraseña es segura o muy segura
        digitos = any(c.isdigit() for c in n)
        letras = any(c.isalpha() for c in n)
        simbolos = any(c.isalnum() == False for c in n)

        if digitos and letras and simbolos:
            print('Contraseña muy segura')
        elif digitos and letras:
            print('Contraseña segura')
        else:
            print('Contraseña Normal')
                        
cont('#20005gagsdhah')