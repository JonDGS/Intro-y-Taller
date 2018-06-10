class matriz():
    def __init__(self):
        pass
    def generar(self,n,m):
##    n = eval(input('Digite la cantidad de filas que quiere: '))
##    m = eval(input('Digite la cantidad de columnas que quiere: '))
        if isinstance(n,int) and isinstance(m,int):
            return self.procesar(0,0,n,m,[],[])
        else:
           return 'Matriz imposible de generar'
    def procesar(self,l,c,n,m,line,new):
        if n == l:
            return new
        elif c == m:
            return self.procesar(l+1,0,n,m,[],new + [line])
        elif l == 0 or l == n-1:
            return self.procesar(l,c+1,n,m,line + ['*'],new)
        elif c == 0 or c == m-1:
           return self.procesar(l,c+1,n,m,line + ['*'],new)
        else:
            return self.procesar(l,c+1,n,m,line + [0],new)
            
