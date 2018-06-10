import time
def validarpares():
    num = eval(input("Ingrese el valor del numero: "))
    if isinstance(num, int):
        return validar(num)
    else:
        print ("Ingrese un valor entero")
        t.sleep(2)
        return validarpares()

def validar(num):
    if (num == 0):
        return 0
    else:
        if num % 10 % 2 == 0:
            return 1 + validar(num // 10)
        else:
            return validar(num // 10)
