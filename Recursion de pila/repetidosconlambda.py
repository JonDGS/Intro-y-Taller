def lista(lista1, num):
    if isinstance(lista1 ,list) and isinstance(num, int):
        x = lambda num1, num2: num1 == num2
        return detectar(lista1,num, x)
    else:
        return 'No se digito una lista'

def detectar(lista1,num1,esto):  
    if lista1 == []:
        return 0
    if esto(lista1[0], num1):
        return 1 + detectar(lista1[1:],num1, esto)
    else:
        return detectar(lista1[1:],num1, esto)
