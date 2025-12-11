def es_digito(s):
    try:
        # Intentar convertir a entero para verificar si está en el rango de 0 a 9
        n = int(s)
        return 0 <= n <= 9
    except ValueError:
        # Si la conversión a entero falla, no es un dígito
        return False
def main ():
    n = input (" Escribe un caracter o ' fin ' para terminar : ")
    if ( es_digito (n)):
        print (n, "es un digito de 0 a 9")
    else :
        print (n, "no es un digito de 0 a 9")
    while n != "fin":
        return main()
        if ( es_digito ('fin')):
            break