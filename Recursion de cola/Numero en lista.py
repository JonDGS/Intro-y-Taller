def  fun(x,lista):
    if isinstance(x, int) and isinstance(lista,list):
        return procesar(x,lista,0)
    else:
        return 'No es una lista'
def procesar(x,lista,i):
    if i == len(lista):
        return False
    elif isinstance(lista[i],list):
        if (procesar(x,lista[i],0)) == False:
            return (procesar(x,lista,i+1))
        else:
            return True
    elif lista[i] == x:
        return True
    else : return procesar (x,lista,i+1)
    
