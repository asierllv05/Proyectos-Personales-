# Solicitar al usuario que ingrese el día, mes y año de nacimiento
dia = int(input("Introduce tu día de nacimiento: "))
mes = int(input("Introduce tu mes de nacimiento: "))
año = int(input("Introduce tu año de nacimiento: "))

# Calcular las cifras del PIN
p1 = (dia // 10 + dia % 10) % 10
p2 = (mes // 10 + mes % 10) % 10
p3 = (año // 1000 + año % 10) % 10
p4 = ((año // 100) % 10 + (año // 10) % 10) % 10

# Mostrar el PIN resultante
print(f"Tu PIN es {p1} {p2} {p3} {p4}")