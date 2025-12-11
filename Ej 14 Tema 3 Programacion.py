divisor=int(input('Dame un numero: '))
dividendo=int(input('Dame un numero: '))
a=divisor / dividendo
b=divisor % dividendo
if dividendo<=0 or divisor<0 :
    print('No se puede dividir entre 0 o numeros negativos')
else:
    print('El coeficiente es:',int(a))
    print('El resto es :',b)
    
    