#1.
def pares(num):
    if isinstance(num,int):
        return procesar(num)
    else:return 'El valor ingresado no es un entero'
def procesar(num):
    if num == 0:
        return []
    elif (num%10)%2==0:
        return [num%10] + procesar(num//10)
    else:
        return procesar(num//10)
#------------------------------------------------------------------------------------------------------------
#2.
def palindromo(num):
    num1 = num
    if isinstance(num,int) and num > 0:
        return contador(num, -1, num1)
    else: ' No es un valor entero o mayor a 0'
def contador(num, d,num1):
    if num == 0:
        return procesar1(0,num1,d)
    else:
        return contador(num//10,d+1,num1)
def procesar1(num1,num2,d):
    if num1 == num2:
        return True
    elif num1 != num2 and d == -1:
        return False
    else:
        return procesar1(num1 + ((num2%10**(d))*10**(d)), num2, d-1)
#-----------------------------------------------------------------------------------------------------------
#3.
def cadena(pa):
    pal = pa
    if isinstance(pal,str):
        return contar(pal)
    else: return 'No es un string'
def contar(pal):
    if pal == '':
        #Nota: en el examen la siguiente linea esta como "return ''" no como se muestra en esta progra
        return 0
    elif pal[0] == 'a' or pal[0] == 'e' or pal[0] == 'i' or pal[0] == 'o' or pal[0] == 'u':
        return contar(pal[1:])
    else:
        return 1 + contar(pal[1:])
#-----------------------------------------------------------------------------------------------------------
#4.
def posiciones(lista):
    if isinstance(lista,list):
        return procesar2(lista)
    else: return 'No es una lista'
def procesar2(lista):
    if lista == []:
        return []
    else:
        return [lista[1]] + [lista[0]] + procesar2(lista[2:])
