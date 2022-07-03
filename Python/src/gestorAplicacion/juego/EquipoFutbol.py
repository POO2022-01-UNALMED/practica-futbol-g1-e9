from .ClubDeportivo import ClubDeportivo


class EquipoFutbol(ClubDeportivo):
    """
    Esta clase permite crear y manejar los equipos de futbol y sus atributos.
    Los atributos de goles, puntos, etc son referentes a la liga que esta en juego.
    @author Sebastian Valencia
    @author Mateo Canavera
    
    """

    def __init__(self, nombre, ubicacion,presupuesto=100000000,entrenador=None, plantilla=[]):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self._entrenador = entrenador
        self._presupuesto = presupuesto
        self._plantilla = plantilla

        self._liga = None

        self._victorias = 0
        self._empates = 0
        self._derrotas = 0
        self._golesAnotados = 0
        self._golesRecibidos = 0
        self._puntos = 0
        self._partidosJugados = 0

    # Getters y setters

    def getPresupuesto(self):
        return self._presupuesto

    def setPresupuesto(self, presupuesto):
        self._presupuesto = presupuesto

    def getVictorias(self):
        return self._victorias

    def setVictorias(self, victorias):
        self._victorias = victorias

    def getEmpates(self):
        return self._empates

    def setEmpates(self, empates):
        self._empates = empates

    def getDerrotas(self):
        return self._derrotas

    def setDerrotas(self, derrotas):
        self._derrotas = derrotas

    def getGolesAnotados(self):
        return self._golesAnotados

    def setGolesAnotados(self, golesAnotados):
        self._golesAnotados = golesAnotados

    def getGolesRecibidos(self):
        return self._golesRecibidos

    def setGolesRecibidos(self, golesRecibidos):
        self._golesRecibidos = golesRecibidos

    def getPuntos(self):

        return self._puntos

    def setPuntos(self, puntos):
        self._puntos = puntos

    def getPartidosJugados(self):
        return self._partidosJugados

    def setPartidosJugados(self, partidosJugados):

        self._partidosJugados = partidosJugados

    def getPlantilla(self):
        return self._plantilla

    def setPlantilla(self, plantilla):
        self._plantilla = plantilla

    def getEntrenador(self):
        return self._entrenador

    def setEntrenador(self, entrenador):

        if self._entrenador is not None:
            self._entrenador.setEquipo(None)

    def getLiga(self):
        return self._liga

    def setLiga(self, liga):
        self._liga = liga

    def registrarPartido(self, golesAnotados, golesRecibidos):

        """
        Registrar un partido jugado por el equipo.
        Calcula los puntos y modifica la cuenta global de los atributos involucrados segun el resultado.
        
        """

        self.setGolesAnotados(self.getGolesAnotados() + golesAnotados)
        self.setGolesRecibidos(self.getGolesRecibidos() + golesRecibidos)
        self.setPartidosJugados(self.getPartidosJugados() + 1)

        if golesAnotados > golesRecibidos:

            self._puntos += 3
            self._victorias += 1

        elif golesAnotados == golesRecibidos:

            self._puntos += 1
            self._empates += 1

        else:

            self._derrotas += 1

    def anadirJugador(self, jugador):

        """Le agrega un jugador a la plantilla del equipo"""

        self._plantilla.append(jugador)
        jugador.setEquipo(self)

    def reestablecerEstadisticas(self):

        """ Reestablece todas las estadisticas del equipo guardadas durante la liga"""

        self._victorias = 0
        self._empates = 0
        self._derrotas = 0
        self._golesAnotados = 0
        self._golesRecibidos = 0
        self._puntos = 0

    def __str__(self):

        return "Nombre: " + str(self.nombre) + " Ubicado en : " + str(
            self.ubicacion) + " Con un Presupuesto de: " + str(
            self._presupuesto) + " y su entrenador se llama:" + str(self._entrenador)
