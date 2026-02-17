Oerrores=0
UTerrores=0
Cerrores=0
for i in range(1,16):
    while True:
        fallos=int(input(f"Introduce la cantidad de fallos encontrado por test {i} :"))
        if fallos >= 0:
            break
        else:
            print("Por favor, ingrese un número natural (mayor o igual a 0).")
    if fallos == 0:
        Oerrores += 1
    elif 1 <= fallos <= 3:
        UTerrores += 1
    else:
        Cerrores += 1
        
print(f"Tests sin errores: {Oerrores}")
print(f"Tests con 1 a 3 errores: {UTerrores}")
print(f"Tests con más de 4 errores: {Cerrores}")
        
        
    
