def suma(lista):
    # if type(lista) == lista
    if isinstance(lista, list):
        return suma_aux(lista)
    else: return 'Error no se ingreso una lista'
def suma(lista):
    if lista == []:
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + suma(lista[1:])
    else: return suma(lista[1:])
