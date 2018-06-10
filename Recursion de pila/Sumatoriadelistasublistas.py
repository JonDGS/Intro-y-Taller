def sumar(lista):
    if isinstance(lista,list):
        return sumar_lista(lista, 0)
    else: return 'El objeto no es una lista'

def sumar_lista(lista,p):
    if lista == []:
        return 0
    else:
        if isinstance(lista[0],list):
            return sumar_lista(lista[0] + lista[1:],p+len(lista[0]))
        else:
            return lista[0]**(p+1) + sumar_lista(lista[1:],p+1)
