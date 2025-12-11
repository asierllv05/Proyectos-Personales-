algo_imp=input("Escribe algo importante: ")

longitud_texto= len(algo_imp) + len(" es importante!")

blancos=longitud_texto-1

print(" "*(blancos//2-1),'\|||||/')

print(" "*(blancos//2-1),'( O O )')

print("|","-"*((blancos-18)//2),'ooO-----(_)',"-"*((blancos-7)//2),"|")

print("|"," "*blancos,"|")

print('|',algo_imp,'es importante!|')

print("|"," "*blancos,"|")

print("|","-"*(blancos//2+4),'Ooo',"-"*((blancos-17)//2),"|")

print(" "*(blancos//2),'|_||_|')

print(" "*(blancos//2),'||  ||')

print(" "*(blancos//2-1),'ooO  Ooo')
