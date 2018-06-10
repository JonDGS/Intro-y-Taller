def matrices(matriz):
	if isinstance(matriz,list):
		return procesar(matriz,0,0,0)
	else: 'Matriz no valido'
def procesar(matriz,i,i2,suma):
    if len(matriz) == i:
        return suma/(len(matriz)*len(matriz[0]))
    elif i2 == len(matriz[i]):
        return procesar(matriz,i+1,0,suma)
    else:
        return procesar(matriz,i,i2+1,suma + matriz[i][i2])
