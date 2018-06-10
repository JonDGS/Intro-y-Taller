def suma(lista):
    num = eval(input('Digite el numero que desea eliminar: '))
    # if type(lista) == lista
    if isinstance(lista, list):
        if isinstance(num, int) and num > 0:
            return suma_aux(lista, num)
        else: return 'Error'
    else: return 'Error no se ingreso una lista'
    
def suma_aux(lista, num):
    if lista == []:
        return []
    if lista[0] == num:
        return suma_aux(lista[1:], num)
    else:
        return [lista[0]] + suma_aux(lista[1:], num)
 

