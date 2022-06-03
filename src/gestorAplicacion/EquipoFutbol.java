package gestorAplicacion;
public class EquipoFutbol extends ClubesDeportivos{
	
	private String nombre;
	private Jugador [] jugadores;
	private int victorias;
	private int derrotas;
	private int empates;
	private int puntos;
	private int golesrecibidos;
	private int golesanotados;
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public Jugador[] getJugadores() {
		return jugadores;
	}
	public void setJugadores(Jugador[] jugadores) {
		this.jugadores = jugadores;
	}
	
	public int getVictorias() {
		return victorias;
	}
	public void setVictorias(int victorias) {
		this.victorias = victorias;
	}
	public int getDerrotas() {
		return derrotas;
	}
	public void setDerrotas(int derrotas) {
		this.derrotas = derrotas;
	}
	public int getEmpates() {
		return empates;
	}
	public void setEmpates(int empates) {
		this.empates = empates;
	}
	public int getPuntos() {
		return puntos;
	}
	public void setPuntos(int puntos) {
		this.puntos = puntos;
	}
	public int getGolesrecibidos() {
		return golesrecibidos;
	}
	public void setGolesrecibidos(int golesrecibidos) {
		this.golesrecibidos = golesrecibidos;
	}
	public int getGolesanotados() {
		return golesanotados;
	}
	public void setGolesanotados(int golesanotados) {
		this.golesanotados = golesanotados;
	}
	
	

}
