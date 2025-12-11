def es_digito(s):
    try:
        # Intentar convertir a entero para verificar si está en el rango de 0 a 9
        n = int(s)
        return 0 <= n <= 9
    except ValueError:
        # Si la conversión a entero falla, no es un dígito
        return False
        
