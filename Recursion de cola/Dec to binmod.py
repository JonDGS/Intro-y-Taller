def dectobin():
    num = eval(input('Digite el base 10 que sea procesar: '))
    if num > 0:
        return binpos(num)
    if num < 0:
        return binneg(num)
    else: return 'El valor ingresado no es un numero valido'
def binpos(num):
    if num == 0:
        return ''
    elif num % 2 == 1:
        return binpos(num // 2) + '1'
    else:
        return binpos(num // 2) + '0'
#---------------------------------------------------------------------------------------------------
def bintodec(num):
    x = num
    if isinstance(num, int):
        return validar(str(num),num)
def validar(x, num):
    if len(x) == 1 and x[0] == '1' or x[0] == '0':
        return convertir(str(num), len(str(num))-1)
    elif x[0] == '1' or x[0] == '0' :
        return validar(x[1:], num)
    else:
        return 'El valor no es un numero en base 10'
def convertir(num,d):
    if num == '1':
        return 1
    if num == '0':
        return 0
    elif num[0] == '1':
        return 2 ** (d) + convertir((num[1:]), d - 1)
    else:
        return convertir((num[1:]), d - 1)
