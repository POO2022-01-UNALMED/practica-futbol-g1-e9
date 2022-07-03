from .IntegranteEquipo import IntegranteEquipo

from enum import Enum


class Jugador(IntegranteEquipo):
    """
    Los Jugadores hacen parte de la plantilla de un EquipoFutbol.
    
    @author Sebastian Valencia
    @author Mateo Canavera
    """

    class Posicion(Enum):
        """ Un enum que permite listas las posibles posiciones en que juega"""

        PT = 0
        DF = 1
        MC = 2
        DL = 3

    def __init__(self, nombre: str, posicion: Posicion, valorMercado: int = 10):
        self._nombre: str = nombre
        self._posicion = posicion
        self._valorMercado: int = valorMercado

        self._equipo = None

    # Getters y setters

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getPosicion(self) -> Posicion:
        return self._posicion

    def setPosicion(self, posicion: Posicion):
        self._posicion = posicion

    def getValorMercado(self) -> int:
        return self._valorMercado

    def setValorMercado(self, valorMercado: int):
        self._valorMercado = valorMercado

    def getEquipo(self):
        return self._equipo

    def setEquipo(self, equipo):
        self._equipo = equipo

    # Se define lo que se va a imprimir
    def __str__(self) -> str:
        return self.getNombre() + ", posicion: " + str(self.getPosicion().name) + ", precio: " + str(
            self.getValorMercado())


"""
# Para hacer pruebas

if __name__ == "__main__":
    j1 = Jugador("Ter Stegen", Jugador.Posicion.PT, 1200)
    
    print(j1)
"""
