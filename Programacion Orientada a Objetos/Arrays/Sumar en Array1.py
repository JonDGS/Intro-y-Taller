class Suma:
    def __init__(self):
        self.resultado = 0
    def sumar(self, lista):
        #resultado = 0
        for valor in lista:
            self.resultado += valor
        return self.resultado
