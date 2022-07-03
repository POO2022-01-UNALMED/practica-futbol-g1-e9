from .IntegranteEquipo import IntegranteEquipo

class Entrenador(IntegranteEquipo):
    """
    Los Entrenadores hacen parte de los EquipoFutbol.

    @author Sebastian Valencia
    @author Mateo Canavera
    
    """

    def __init__(self, nombre: str, equipo=None):
        self._nombre: str = nombre
        self._equipo = equipo

    # Getters y setters

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEquipo(self):
        return self._equipo

    def setEquipo(self, equipo):
        self._equipo = equipo

    def ficharJugador(self, jugador):
        """ Para que el entrenador pueda comprar jugadores"""

        # Aca se puede crear una excepcion para un entrenador que 
        # 1. Quiera fichar pero no pertenezca a un equipo 
        # 2. El equipo no tenga dinero suficiente

        self._equipo.setPresupuesto(self._equipo.getPresupuesto() - jugador.getValorMercado())
        self._equipo.anadirJugador(jugador)
        self._equipo.getLiga().getJugadoresLibres().remove(jugador)

    def __str__(self):
        """Se redefine lo que se va a mostrar al imprimir"""

        return self.getNombre()
