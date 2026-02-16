PCerveza=float(input('¿Precio cerveza? :'))
PVino=float(input('¿Precio Vino? :'))
PPatatas=float(input('¿Precio Patatas Fritas? :'))
CCerveza=float(input('¿Cantidad cerveza? :'))
CVino=float(input('¿Cantidad Vino? :'))
CPatatas=float(input('¿Cantidad Patatas Fritas? :'))
TCerveza=PCerveza*CCerveza
TVino=PVino*CVino
TPatatas=PPatatas*CPatatas



Compra = ' ¿Precio cerveza? {}\n ¿Precio vino? {}\n ¿Precio patatas fritas? {}\n ¿Cuanta cerveza? {}\n ¿Cuanto vino? {}\n ¿Cuantas patatas fritas? {}'.format(PCerveza,PVino,PPatatas,CCerveza,CVino,CPatatas)
print(Compra)
print('-----------------------------')
print('Total Compra')
print('-----------------------------')
Factura= ' Cerveza        {} {}\n Vino           {}  {}\n Patatas Fritas {}    {}'.format(CCerveza,TCerveza,CVino,TVino,CPatatas,TPatatas)
print(Factura)
print('                    -----')
print(' '*13,'total',TVino+TCerveza+TPatatas)         