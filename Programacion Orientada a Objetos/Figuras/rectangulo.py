from Clases import Fig
import math
class Rectangulo(Fig):
    def __init__(self,x,y,alto,ancho):
        super().__init__(x,y)
        self.__alto = alto
        self.__ancho = ancho
    def getAlto(self):
        return self.__alto
    def setAlto(self,alto):
        self.__alto = alto
    def getAncho(self):
        return self.__ancho
    def setAncho(self,ancho):
        self.__ancho = ancho
    def calcularArea(self):
        return self.__alto * self.__ancho
        
