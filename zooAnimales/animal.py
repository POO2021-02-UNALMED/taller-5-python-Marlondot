class Animal:
    _zona=list()
    _totalAnimales=0
    
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
    
    #
    #getting and setting
    #

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad

    def setEdad(self,edad):
        self._edad=edad
    
    def getHabitat(self):
        return self._habitat

    def setHabitat(self,habitat):
        self._habitat=habitat

    def getGenero(self):
        return self._genero

    def setGenero(self,genero):
        self._genero=genero

    @classmethod
    def getZona(cls):
        return cls._zona

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    #
    #methods
    #
    
    #this one could be a static method(?)
    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        answer=("Mamiferos: {}\n"
				+ "Aves: {}\n"
				+ "Reptiles: {}\n"
				+ "Peces: {}\n"
				+ "Anfibios: {}")[0].format(Mamifero.cantidadMamiferos(),Ave.cantidadAves(),Reptil.cantidadReptiles(),Pez.cantidadPeces(),Anfibio.cantidadAnfibios())
        return answer
    
    def toString(self):
        if self._zona==[]:
            answer="Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self._nombre,self._edad,self._habitat,self._genero)
            return answer
        else:
            answer="Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}, la zona en la que me ubico es {}, en el {}".format(self._nombre,self._edad,self._habitat,self._genero,self._zona,self._zona[0].getZoo())
            return answer

