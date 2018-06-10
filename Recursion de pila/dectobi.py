def dectobin(num):
    #num = eval(input('Digite el base 10 que sea procesar: '))
    if num > 0:
        return binpos(num,[])
    if num < 0:
        return binneg(num)
    else: return 'El valor ingresado no es un numero'
def binpos(num,lista):
    if num == 0:
        return volver(lista, [])
    elif num % 2 == 1:
        return binpos((num//2),lista + [1])
    else:
        return binpos((num//2),lista + [0])
def volver(lista, nueva):
    if lista == []:
        return nueva
    else:
        return volver(lista[:-1],nueva + [lista[-1]])
