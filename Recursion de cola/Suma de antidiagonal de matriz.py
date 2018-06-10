def sumarAntiDiagonal(matriz):
    if isinstance(matriz,list) and matriz != []:
        return sumarAntiDiagonal1(matriz,len(matriz)-1, 0, 0)
    else: return " Error no es una lista"

def sumarAntiDiagonal1(matriz,indice1,indice2,resultado):
    if indice1==-1:
        return resultado
    else: return sumarAntiDiagonal1(matriz,indice1-1,indice2+1,resultado +matriz[indice1][indice2])
