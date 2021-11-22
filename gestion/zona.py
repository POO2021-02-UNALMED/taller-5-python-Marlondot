class Zona:
    _zoo=None 

    def __init__(self,nombre,zoo):
        self._nombre=nombre
        Zona._zoo=zoo
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
    
    @classmethod
    def getZoo(cls):
        return cls._zoo

    @classmethod
    def setZoo(cls,zoo):
        cls._zoo=zoo

    #
    #Methods
    #

    def agregarAnimales(self,animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        self._animales.count()
    

