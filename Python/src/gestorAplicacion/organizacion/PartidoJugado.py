from gestorAplicacion.organizacion.Partido import Partido

class PartidoJugado(Partido):

    def __init__(self, partido, golesLocal, golesVisitante):

        self.equipoLocal = partido.getEquipoLocal()
        self.equipoVisitante = partido.getEquipoVisitante()
        self.arbitro = partido.getArbitro()
        self._golesLocal = golesLocal
        self._golesVisitante = golesVisitante


#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public PartidoJugado()
    def __init__(self):
        self._initialize_instance_fields()

        super().__init__()

    def getGolesLocal(self):
        return self._golesLocal

    def setGolesLocal(self, golesLocal):
        self._golesLocal = golesLocal

    def getGolesVisitante(self):
        return self._golesVisitante

    def setGolesVisitante(self, golesVisitante):
        self._golesVisitante = golesVisitante


    def toString(self):
        return "\n" + self.equipoLocal.getNombre() + " " + str(self._golesLocal) + " - " + str(self._golesVisitante) + " " + self.equipoVisitante.getNombre()
