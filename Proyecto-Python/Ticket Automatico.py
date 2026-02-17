
cantidad_rebanadas = int(input("Por favor, ingrese la cantidad de rebanadas de pan que desea comprar: "))
precio_por_rebanada = 3.49
precio_sin_descuento = cantidad_rebanadas * precio_por_rebanada
descuento = 0.0
if cantidad_rebanadas > 0:
    descuento = precio_sin_descuento * 0.60
precio_total = precio_sin_descuento - descuento
print("Barras de Pan:         ",cantidad_rebanadas)
print("------------------------------")
print("Precio del pan:        ",precio_por_rebanada*cantidad_rebanadas)
print("Descuento :            ",descuento)
print("------------------------------")
print("Precio total:           {:.2f} ".format(precio_total))
