nh=float(input('Introduce el numero de horas trabajadas:'))
ph=float(input('Introduce el precio de dichas horas:'))
r=float(input('Introduce la retención aplicable en tanto por cien:'))
SB=nh*ph
SN=SB-(r/100*SB)
print('El salario bruto es :',SB)
print('El salario neto es :',SN)