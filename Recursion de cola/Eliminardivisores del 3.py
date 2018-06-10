def eliminar(num):
    if isinstance(num, int):
        return eliminar_aux(num,0,0)
    else:
        return 'No es un numero valido'
def eliminar_aux(num, d,new):
    if num == 0:
        return new
    elif (num%10) % 3 == 0:
        return eliminar_aux(num//10, d, new)
    else: return eliminar_aux(num // 10, d+1, new + ((num%10)*10**d)) 
        
