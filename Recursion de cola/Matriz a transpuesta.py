def transpuesta_de_matriz(matriz):
    if isinstance(matriz,list):
        return procesar(matriz,0,0,[],[])
    else: 'Matriz no valido'
def procesar(matriz,i,i2,obj,new):
    if i2 == len(matriz[0]):
        return new
    elif i2 == len(matriz):
        return procesar(matriz,0,i2+1,[],new + obj)
    else:
        return procesar(matriz,i+1,i2,new + [matriz[i][i2]],new)
