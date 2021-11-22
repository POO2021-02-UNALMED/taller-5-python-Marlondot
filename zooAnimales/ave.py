from zooAnimales.animal import Animal

class Ave(Animal):
    _listado=list()
    halcones=0
    aguilas=0

    def __init__(self,nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas

        Ave._listado.append(self)

    #
    #getting and setting
    #

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas

    #
    #methods
    #

    @classmethod
    def cantidadAves(cls):
        return cls._listado

    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones+=1
        return Ave(nombre, edad, "montanas",genero,"cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas+=1
        return Ave(nombre, edad, "selva",genero,"blanco y amarillo")
