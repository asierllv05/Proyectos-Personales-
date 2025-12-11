def es_divisor(dividendo, divisor):
    if divisor == 0:
        return True
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    menor_numero = min(dividendo, divisor)
    while dividendo >= divisor:
        dividendo -= divisor
    if dividendo == 0:
        return True
    else:
        return False
dividendo = int(input("Ingresa el dividendo (número entero): "))
divisor = int(input("Ingresa el divisor (número entero): "))

if es_divisor(dividendo, divisor):
    print(f"{divisor} es divisor de {dividendo}.")
else:
    print(f"{divisor} no es divisor de {dividendo}.")
