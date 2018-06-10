def suma(lista):
    # if type(lista) == lista
    if isinstance(lista, list):
        return suma_aux(lista)
    else: return 'Error no se ingreso una lista'
def suma_aux(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + suma_aux(lista[1:])
