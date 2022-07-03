from gestorAplicacion.organizacion.Partido import Partido


class Fixture(Partido):
    """
    Partido con detalles de su planeación para jugarse proximamente.
    
    @author Sebastian Valencia
    @author Mateo Canavera
    """

    def __init__(self, equipoLocal, equipoVisitante, arbitro = None):
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.arbitro = arbitro

    def setArbitro(self, arbitro):
        """ Se coloca solo en Fixture y no en Partido
            porque a un PartidoJugado no se le puede reasignar el Arbitro.

            También aumenta el número de partidos del árbitro nuevo
            y disminuye el del anterior si había uno.
        """

        if self.arbitro is not None:
            self.arbitro.setPartidos(arbitro.getPartidos() - 1)

        self.arbitro = arbitro
        arbitro.setPartidos(arbitro.getPartidos() + 1)

    def __str__(self):
        return self.equipoLocal.nombre + " vs " + self.equipoVisitante.nombre
