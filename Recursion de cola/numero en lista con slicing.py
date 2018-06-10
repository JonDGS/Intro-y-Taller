def  fun(x,lista):
    if isinstance(x, int) and isinstance(lista,list):
        return procesar(x,lista)
    else:
        return 'No es una lista'
def procesar(x,lista):
    if lista == []:
        return False
    elif isinstance(lista[0],list):
        if (procesar(x,lista[0])) == False:
            return procesar(x,lista[1:])
        else:
            return True
    elif lista[0] == x:
        return True
    else: return procesar(5,lista[1:])
