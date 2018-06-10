def listas(lista):
    if isinstance(lista,list):
        return high(lista,0,lista[0]), low(lista,0,lista[0])
    else:
        return 'El valor no es valido'
def high(lista,i,m):
    if i == len(lista):
        return m
    elif isinstance(lista[i],list):
        return high((([lista[i:]] + [(high(lista[i],0,1))]),i+1, m))
    elif lista[i] > m:
        return high(lista,i+1,(m*0) + lista[i])
    else:
        return high(lista,i+1,m)
def low(lista,i,l):
    if i == len(lista):
        return l
    elif isinstance(lista[i],list):
        return low((([lista[i:]] + [(low(lista[i],0,1))]),i+1, l)) 
    elif lista[i] < l:
        return low(lista,i+1,(l*0) + lista[i])
    else:
        return low(lista,i+1,l)
    
