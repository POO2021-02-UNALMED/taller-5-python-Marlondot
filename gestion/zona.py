#from zoologico import Zoologico

class Zona:

    def __init__(self,nombre,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=list()

    #
    #Getting and setting
    #
        
    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getAnimales(self):
        return self._animales

    def setAnimales(self,animales):
        self._animales=animales
    
    #@classmethod
    def getZoo(self):
        return self._zoo

    #@classmethod
    def setZoo(self,zoo):
        self._zoo=zoo

    #
    #Methods
    #

    def agregarAnimales(self,animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        len(self._animales)


    

