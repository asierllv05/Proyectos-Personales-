monto_compra = float(input("Ingrese el monto de la compra: "))
es_socio = input("¿Es usted socio? (Sí o No): ").lower()

descuento = 0

if monto_compra >= 10:
    if es_socio == "sí" or es_socio == "si":
        if monto_compra <= 20:
            descuento = monto_compra * 0.05  
        else:
            descuento = monto_compra * 0.12  
    else:
        if monto_compra > 20:
            descuento = monto_compra * 0.06  

total_a_pagar = monto_compra - descuento
print(f"Total a pagar:,",total_a_pagar,"euros")
