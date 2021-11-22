class Zoologico():
    _zonas=list()

    def __init__(self,nombre,ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion

    #
    #getting and setting
    #

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    
    @classmethod
    def getZonas(cls):
        return cls._zonas

    #
    #methods
    #

    @classmethod
    def agregarZonas(cls,zona):
        cls._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        count=0
        for zona in cls._zonas:
            count+=zona.cantidadAnimales()
        
        return count
    
