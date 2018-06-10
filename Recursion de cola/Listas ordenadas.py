def ordenar(lista):
    if isinstance(lista,list):
        return orden(lista,0,0)
    else: return 'No es una lista'
def orden(lista,i,i2):
    if i2 == len(lista) -1:
        return lista
    elif i == len(lista) - 1:
        return orden(lista,0,i2 + 1)
    elif lista[i] > lista[i+1]:
        #aux = lista[i]
        #lista[i] = lista[i+1]
        #lista[i+1] = aux
        lista[i], lista[i+1] = lista[i+1], lista[i]
    return orden(lista, i + 1, i2)
    

    
        
