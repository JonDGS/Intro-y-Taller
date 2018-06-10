def lista(lista1):
    if isinstance(lista1 ,list):
        x = lambda num: num == 0
        return detectar(lista1, x)
    else:
        return 'No se digito una lista'

def detectar(lista1,esto):  
    if lista1 == []:
        return False
    if (esto(lista1[0])):
        return True
    else:
        return detectar(lista1[1:], esto)
