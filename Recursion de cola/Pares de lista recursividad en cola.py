def x(lista):
    if isinstance(lista, list):
        return auxiliar(lista,len(lista),0,[])
    else:
        return 'No es una lista'
def auxiliar(lista,l,i,new):
    if i == l:
        return new
    elif lista[0] % 2 == 0:
        return auxiliar(lista[1:],l,i+1,new + [lista[0]])
    else:
        return auxiliar(lista[1:],l,i+1,new)
        
        
