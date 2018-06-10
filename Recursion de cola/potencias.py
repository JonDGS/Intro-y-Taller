def potencia(num):
    if isinstance(num, int) and (num > 0):
        return algo(num)
    else:
        print("El valor no es valido")
def algo(num):
    if num == 0:
        return 1
    else:
        print(2 ** num)
        return algo(num-1)
