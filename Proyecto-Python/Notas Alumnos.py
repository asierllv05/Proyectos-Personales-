calificaciones = []
aprobados = 0
suspendidos = 0
suma_calificaciones = 0

while True:
    entrada = input("Ingrese la calificación del alumno (o escriba 'exit' para terminar): ")
    
    if entrada.lower() == 'exit':
        break
    
    calificacion = float(entrada)
    
    if calificacion >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    
    suma_calificaciones += calificacion
    calificaciones.append(calificacion)

if len(calificaciones) > 0:
    calificacion_media = suma_calificaciones / len(calificaciones)
else:
    calificacion_media = 0

print(f"Número de aprobados: {aprobados}")
print(f"Número de suspendidos: {suspendidos}")
print(f"Calificación media: {calificacion_media}")
