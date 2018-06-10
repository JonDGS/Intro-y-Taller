def matriz(lista):
    if isinstance (lista,list):
        return procesar(lista,0,0,0,0)
    else: return 'No es valido'
def procesar(lista,i,i2,d,suma):
    if i == len(lista):
        return suma
    elif i2 == len(lista[i]):
        return procesar(lista,i+1,0,d+1,suma)
    elif not isinstance(lista[i],list) and i>0:
        return 'Esto no es una matriz'
    elif i2 == d:
        return procesar(lista,i,i2+1,d,suma + lista[i][i2])
    else:
        return procesar(lista,i,i2+1,d,suma)
