class Partido:
    """
    Los Partidos son los eventos de interés que cambiando en el transcurso de la liga.
    Esta pretende ser una clase abstracta de la cuál se creen dos tipos de instancias:
        1. Fixture: Partido con detalles de su planeación para jugarse proximamente.
        2. PartidoJugado: Partido ya jugado del que se guardan resultados.
    
    @author Sebastian Valencia
    @author Mateo Canavera
    """

    # Getters y Setters

    def getEquipoLocal(self):
        return self.equipoLocal

    def setEquipoLocal(self, equipoLocal):
        self.equipoLocal = equipoLocal

    def getEquipoVisitante(self):
        return self.equipoVisitante

    def setEquipoVisitante(self, equipoVisitante):
        self.equipoVisitante = equipoVisitante

    def getArbitro(self):
        return self.arbitro

    def __str__(self):

        if self.arbitro is None:
            return "\n" + self.getEquipoLocal().getNombre() + " vs " + self.getEquipoVisitante().getNombre() + "\n" + self.getEquipoLocal().getUbicacion() + " | Arbitro: Por definir"
        else:
            return "\n" + self.getEquipoLocal().getNombre() + " vs " + self.getEquipoVisitante().getNombre() + "\n" + self.getEquipoLocal().getUbicacion() + " | Arbitro: " + self.getArbitro()
