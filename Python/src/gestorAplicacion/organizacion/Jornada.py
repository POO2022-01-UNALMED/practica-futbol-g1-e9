import datetime


class Jornada:
    def __init__(self, partidos):
        self._partidos = partidos
        self._fecha = None
        self._jugada = False

    # Getters y setters

    def getPartidos(self):
        return self._partidos

    def setPartidos(self, partidos):
        self._partidos = partidos

    def getIndice(self) -> int:
        return self._indice

    def setIndice(self, indice):
        self._indice = indice

    def getFecha(self) -> datetime.datetime:
        return self._fecha

    def setFecha(self, fecha):
        self._fecha = fecha

    def isJugada(self):
        return self._jugada

    def setJugada(self, jugada):
        self._jugada = jugada

    # Metodos

    def agregarPartido(self, partido):
        self._partidos.append(partido)

    def mostrarFecha(self):
        fecha = self.getFecha()

        diaTexto = str(fecha.day)
        mesTexto = str(fecha.month)
        anioTexto = str(fecha.year)

        return diaTexto + " / " + mesTexto + " / " + anioTexto

    def designarFecha(self, fechaInicio):
        """Establece la fecha de la jornada. Las jornadas se juegan cada 7 dias"""

        fecha = fechaInicio + datetime.timedelta(days=(7*(self.getIndice()-1)))

        self.setFecha(fecha)  # Establece la fecha correspondiente

    def designarArbitros(self, arbitros: list):
        """Establece los arbitros de cada partido"""

        i = 0

        for partido in self.getPartidos():
            partido.setArbitro(arbitros[i])
            i += 1


    def __str__(self):
        texto = "Jornada " + str(self.getIndice())

        if self.getFecha() is not None:
            texto += "\nFecha: " + self.getFecha().strftime("%d/%m/%Y")

        for partido in self._partidos:
            texto += "\n" + str(partido)

        texto += "\n"

        return texto
