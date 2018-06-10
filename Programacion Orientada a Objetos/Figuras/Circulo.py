from Clases import Fig
import math
class Circulo(Fig):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__radio = r
    def getRadio(self):
        return self.__radio
    def setRadio(self,r):
        self.__radio = r
    def calcularArea(self):
        return math.pi * (self.__radio**2)
