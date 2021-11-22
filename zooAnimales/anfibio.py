from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado=list()
    ranas=0
    salamandras=0

    def __init__(self,nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso

        Anfibio._listado.append(self)

    #
    #getting and setting
    #

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso

    #
    #methods
    #

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento():
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas+=1
        return Anfibio(nombre, edad, "selva",genero,"rojo",True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras+=1
        return Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False)

    