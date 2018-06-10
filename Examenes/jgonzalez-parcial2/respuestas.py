def invertir(lista):
    if isinstance(lista,list):
        return procesar(lista,0,len(lista))
    else:
        return 'No es una lista'
def procesar(lista,lugar,tamano):
    if lugar == tamano:
        return lista[:tamano]
    else:
        return procesar(lista+[lista[-lugar]],lugar+1,tamano)
#--------------------------------------------------------------------------------------
def consecutivos(array):
    if isinstance(array,list):
        return procesar1(array,(len(array)**2),0,0,0)
    else:
        return 'No es una matriz'
def procesar1(array,length,indice,indice2,contador):
    if length + 1 == contador:
        return True
    elif indice2 == (length**0.5):
        return procesar1(array,length,indice+1,0,contador)
    elif contador == array[indice][indice2]:
        return procesar1(array,length,0,0,contador+1)
    elif indice > ((length)**0.5):
        return False
    else:
        return procesar1(array,length,indice,indice2+1,contador)
#--------------------------------------------------------------------------------------
def es_magico(array):
    if isinstance(array,list):
        return procesar2(array,len(array),0,0,0)
    else:
        return 'No es una matriz valida'
def procesar2(array,length,indice,indice2,sum1):
    if length == indice2:
        return fila(array,length,0,0,sum1,0)
    else:
        return procesar2(array,length,indice,indice2,sum1+array[indice][indice2])
def fila(array,length,indice,indice2,sum1,suma):
    if length == indice:
        return columnas(array,length,0,0,sum1,0)
    elif length == indice2 and sum1 == suma:
        return fila(array,length,indice+1,0,sum1,0)
    elif indice2 > length:
        return False
    else:
        return fila(array,length,indice,indice2+1,sum1,suma + array[indice][indice2])
def columnas(array,length,indice,indice2,sum1,suma):
    if indice2 == length:
        return diagonal(array,length,0,0,suma1,0)
    elif indice == length and suma == sum1:
        return columnas(array,length,0,indice2+1,sum1,0)
    elif indice > length:
        return False
    else:
        columnas(array,length,indice+1,indice2,sum1,suma)
def diagonal(array,length,indice,indice2,sum1,suma):
    if length == indice and suma == sum1:
        return antidiagonal(array,length,0,0,sum1,0)
    elif indice > length:
        return False
    else:
        return diagonal(array,length,indice+1,indice2+2,sum1,suma+array[indice][indice2])
def antidiagonal(array,length,indice,indice2,sum1,suma):
    if length == indice and suma == sum1:
        True
    elif indice > length:
        return False
    else:
        return antidiagonal(array,length,indice+1,indice2+2,sum1,suma+array[indice][-indice2])
#--------------------------------------------------------------------------------------------------------
def rotar(array):
    if isinstance(array,list):
        return procesar3(array,0,0,[],[])
    else:
        'No es una matriz'
def procesar3(array,fila,columna,new,nueva):
    if fila == len(array):
        return nueva
    elif columna == len(array):
        return procesar3(array,fila+1,0,[],nueva+[new])
    else:
        return procesar3(array,fila,columna+1,new+[array[fila][-columna]],nueva)
   
