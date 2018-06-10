def suma(lista):
    # if type(lista) == lista
    if isinstance(lista, list):
        return suma_aux(lista), suma2(lista)
    else: return 'Error no se ingreso una lista'
def suma_aux(lista):
    if lista == []:
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + suma_aux(lista[1:])
    else: return suma_aux(lista[1:])
def suma2(lista):
    if lista == []:
        return 0
    if (lista[0] % 2) == 1:
        return lista[0] + suma2(lista[1:])
    else: return suma2(lista[1:])
