def primo(num):
    if isinstance(num, int):
        if num == 1 or num == 0:
            print(num,'es un numero especial.')
        else:
            return primo_aux(num,num - 1)
def primo_aux(num,d):
    if d == 1:
        print(num,'es primo.')
    if num % d == 0:
        print(num,'es compuesto')
    elif num % d == 1:
        return primo_aux(num, d-1)
    print('Llego aqui')
    #else:
    #    return primo_aux(num, d-1)
