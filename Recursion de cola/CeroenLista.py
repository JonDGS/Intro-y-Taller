def suma(lista):
    # if type(lista) == lista
    if isinstance(lista, list):
        return suma_aux(lista)
    else: return 'Error no se ingreso una lista'
def suma_aux(lista):
    if lista == []:
        return False
    elif lista[0] == 0:
        return True
    else: return suma(lista[1:])

