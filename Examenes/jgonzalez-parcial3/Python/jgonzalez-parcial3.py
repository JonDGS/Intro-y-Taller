class Examen():
    def __init__(self):
        pass
    def contar(self):
        numero = int(input('Digite un numero: '))
        mazda = 0
        i = numero
        if numero == 0:
            print(numero, "tiene ", mazda + 1, " digitos")
        while (numero // 10) != numero:
            numero = numero // 10
            mazda += 1
        print(i, "tiene ", mazda, "digitos")
#-------------------------------------------------------------------
    def ordenar(self, lista):
        new = []
        length = len(lista)
        for x in range(0, length):
            indice = self.encontrar(self, lista):
            new  += [lista[indice]]
            lista = lista[i-1:] + lista[:i]
        print(new)
    def encontrar(self, lista):
        indice = 0
        minimo = lista[0]
        for x in range(0, len(lista)):
            if minimo > lista[x+1]:
                indice = x+1
                minimo = lista [x+1]
            elif minimo < lista[x+1]:
                pass
            elif minimo = lista[x+1]:
                pass
        return indice
#--------------------------------------------------------------------
    def generar(matriz, matriz1):
        m = len(matriz)
        n = len(matriz[0])
        new = []
        elemento[]
        for x in range(0,m):
            elemento = []
            Temporal = 0
            suma = 0
            for y in range (0,n):
                suma += matriz[indice][y]*matriz1[y][Temporal]
                elemento = [suma]
                new = [[elemento]]
                Temporal += 1
        print(new)
