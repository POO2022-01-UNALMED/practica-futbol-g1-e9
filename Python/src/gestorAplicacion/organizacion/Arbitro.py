# Para designar árbitros a partidos de forma aleatoria
import random


class Arbitro:
    """ Los Arbitros son un atributo que se asigna a los partidos para que
        puedan "ser jugados" y se puedan registrar sus resultados.
        
        @author Sebastian Valencia
        @author Mateo Canavera

    """

    # La clase Arbitro tiene este atributo de clase, ya que estos arbitros estan constituidos
    # independiente de la liga

    # Lista de todos los arbitros:
    federacionArbitros = []

    def __init__(self, nombre: str, salario: int = 1000):
        self._nombre: str = nombre
        self._salario: int = salario
        self._partidos: int = 0
        Arbitro.federacionArbitros.append(self)

    # Getters y setters
    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getSalario(self) -> int:
        return self._salario

    def setSalario(self, salario: int):
        self._salario = salario

    def getPartidos(self) -> int:
        return self._partidos

    def setPartidos(self, partidos: int):
        self._partidos = partidos

    def bonificacionSalario(self):
        """ Falta implementacion!!!!
            Puede ser con la cantidad de partidos pitados, me lo habias propuesto antes"""

        return 0

    @staticmethod
    def listaAleatoriaArbitros():
        """ Devuelve una lista de arbitros en orden aleatorio """

        # Inicializamos la lista aleatoria con los mismo elementos de la original
        # Se le coloca el copy() para no modificar la original con el shuffle
        arbitrosAleatorio = Arbitro.federacionArbitros.copy()

        # Se cambia el orden de la aleatoria
        random.shuffle(arbitrosAleatorio)

        return arbitrosAleatorio

    def __str__(self) -> str:
        return self._nombre

    @classmethod
    def reestablecerArbitros(cls):
        """ Le reestablece el numero de partidos a todos los arbitros """

        for arbitro in cls.federacionArbitros:
            arbitro.setPartidos(0)


"""

Codigo para pruebas:

if __name__ == "__main__":
    a1 = Arbitro("Howard Webb", 1200)
    a2 = Arbitro("Pierluigi Collina")
    a3 = Arbitro("Nestor Pitana")
    a4 = Arbitro("Felix Brycht")

    for a in Arbitro.listaAleatoriaArbitros():
        print(a)
    
    print("")

    for a in Arbitro.federacionArbitros:
        print(a)



# Para la serializacion inicial cuando se haga:
#a1 = Arbitro("Howard Webb", 1200)
#a2 = Arbitro("Pierluigi Collina")
#a3 = Arbitro("Nestor Pitana")
#a4 = Arbitro("Felix Brycht")z

"""
