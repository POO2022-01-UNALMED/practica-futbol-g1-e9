from gestorAplicacion.juego.EquipoFutbol import EquipoFutbol
from gestorAplicacion.juego.Jugador import Jugador
from gestorAplicacion.organizacion.Arbitro import Arbitro
from gestorAplicacion.organizacion.Fixture import Fixture
from gestorAplicacion.organizacion.Jornada import Jornada

from datetime import datetime

import operator
from functools import reduce


class Liga:
    jugadoresLibres = [Jugador("Maradona", Jugador.Posicion.DL, 10000000),
                       Jugador("Messi", Jugador.Posicion.DL, 20000000),
                       Jugador("Cristiano Ronaldo", Jugador.Posicion.DL, 20000000),
                       Jugador("Carles Puyol", Jugador.Posicion.DF, 5000000),
                       Jugador("Pepe", Jugador.Posicion.DF, 4500000),
                       Jugador("Rio Ferdinand", Jugador.Posicion.DF, 7000000),
                       Jugador("Keylor Navas", Jugador.Posicion.PT, 11000000),
                       Jugador("Manuel Neuer", Jugador.Posicion.PT, 15000000),
                       Jugador("Oliver Kahn", Jugador.Posicion.PT, 18000000)]

    equipos = []

    NUMERO_DE_EQUIPOS = 4

    fechaInicio = None

    calendario = []

    # Getters y Setters:

    @classmethod
    def getCalendario(cls):
        return cls.calendario

    @classmethod
    def setCalendario(cls, calendario):
        cls.calendario = calendario

    @classmethod
    def getJugadoresLibres(cls):
        return cls.jugadoresLibres

    @classmethod
    def setFechaInicio(cls, fechaInicio):
        cls.fechaInicio = fechaInicio

    @classmethod
    def getFechaInicio(cls):
        return cls.fechaInicio

    @classmethod
    def getEquipos(cls):
        return cls.equipos

    @classmethod
    def getNumeroDeEquipos(cls):
        return cls.NUMERO_DE_EQUIPOS

    # Metodos

    @classmethod
    def ligaCompleta(cls) -> bool:

        """Permite saber si la liga ya contiene la cantidad de equipos esperada"""

        if len(cls.getEquipos()) == cls.getNumeroDeEquipos():
            return True
        else:
            return False

    @classmethod
    def equipoPertenece(cls, equipo) -> bool:

        """Permite saber un equipo pertenece a la liga"""

        if cls.getEquipos().count(equipo) == 1:
            return True
        else:
            return False

    @classmethod
    def anadirEquipo(cls, equipo):
        cls.equipos.append(equipo)
        equipo.setLiga(cls)

    @classmethod
    def eliminarEquipo(cls, equipo):
        cls.equipos.remove(equipo)
        cls.eliminarCalendario()
        equipo.setLiga(None)

    @classmethod
    def identificarEquipo(cls, nombreEquipo: str):

        """Retorna la instancia del equipo ingresando su nombre"""

        for equipo in cls.equipos:
            if equipo.getNombre() == nombreEquipo:
                return equipo
        return None

    # Se genera el calendario de partidos
    @classmethod
    def generarCalendario(cls):
        equipos = cls.getEquipos().copy()
        first = Liga.fixtures(cls.getEquipos())

        # if you want return matches
        reverse_teams = [list(x) for x in zip(equipos[1::2], equipos[::2])]
        reverse_teams = reduce(operator.add, reverse_teams)

        # then run the fixtures again
        second = Liga.fixtures(reverse_teams)

        calendario = []

        indice = 1

        for i in range(len(second)):
            first[i].setIndice(indice)
            calendario.append(first[i])
            indice += 1

            second[-(i + 1)].setIndice(indice)
            calendario.append(second[-(i + 1)])
            indice += 1

        cls.setCalendario(calendario)

    @staticmethod
    def fixtures(equipos):

        """Genera la mitad de las jornadas"""

        if len(equipos) % 2:
            equipos.append('Day off')

        rotation = list(equipos)  # copy the list

        jornadas = []

        for i in range(0, len(equipos) - 1):
            partidos = [Fixture(rotation[0], rotation[1]),
                        Fixture(rotation[2], rotation[3])]

            jornada = Jornada(partidos)
            jornadas.append(jornada)

            rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

        return jornadas

    @classmethod
    def eliminarCalendario(cls):
        cls.calendario.clear()

        for equipo in cls.equipos:
            equipo.reestablecerEstadisticas()

        for arbitro in Arbitro.federacionArbitros:
            arbitro.setPartidos(0)
            arbitro.setPartidos(1000)

    @classmethod
    def registrarJornada(cls, registroJornada):
        """Falta implementar"""

    @classmethod
    def asignarArbitrosFechas(cls):

        for jornada in cls.calendario:

            # Asignacion de fechas
            jornada.designarFecha(cls.fechaInicio)

            # Asignacion de Arbitros
            arbitros_aleatorios = Arbitro.listaAleatoriaArbitros()
            jornada.designarArbitros(arbitros_aleatorios)

    @classmethod
    def isCalendarioListo(cls):
        if not cls.calendario:
            return False
        elif cls.calendario[0].getFecha() is not None:
            return True
        else:
            return False

    @classmethod
    def proximaJornada(cls):

        numeroProximaJornada = 0

        for jornada in cls.calendario:
            if jornada.isJugada():
                numeroProximaJornada += 1

        return numeroProximaJornada

    @classmethod
    def jugadoresFichables(cls, posicion: Jugador.Posicion, equipo):
        jugadores = []

        for jugador in cls.jugadoresLibres:
            if (jugador.getPosicion() == posicion) and (jugador.getValorMercado() <= equipo.getPresupuesto()):
                jugadores.append(jugador)

        return jugadores


if __name__ == "__main__":

    a1 = Arbitro("Howard Webb", 1200)
    a2 = Arbitro("Pierluigi Collina")
    a3 = Arbitro("Nestor Pitana")
    a4 = Arbitro("Felix Brycht")

    t1 = EquipoFutbol("Barcelona", "Camp Nou")
    t2 = EquipoFutbol("Liverpool", "Anfield")
    t3 = EquipoFutbol("Marsella", "Velodrome")
    t4 = EquipoFutbol("Dortmund", "Signal Iduna Park")

    teams = [t1, t2, t3, t4]
    Liga.anadirEquipo(t1)
    Liga.anadirEquipo(t2)
    Liga.anadirEquipo(t3)
    Liga.anadirEquipo(t4)

    Liga.generarCalendario()

    Liga.setFechaInicio(datetime.now())

    Liga.asignarArbitrosFechas()

    for j in Liga.getCalendario():
        print(j)
