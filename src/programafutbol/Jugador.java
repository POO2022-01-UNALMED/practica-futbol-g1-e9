package programafutbol;

import java.util.ArrayList;

public class Jugador {
	private String nombre;
	private int valorMercado;
	private boolean transferible;
	private int goles;
	private  int asistencias;
	private String posicion;
	ArrayList<Jugador> jugadores = new ArrayList<>();
	
	
	
	public Jugador(String nombre, int valorMercado, boolean transferible, int goles, int asistencias, String posicion) {
		super();
		this.nombre = nombre;
		this.valorMercado = valorMercado;
		this.transferible = transferible;
		this.goles = goles;
		this.asistencias = asistencias;
		this.posicion = posicion;
		jugadores.add(this);
		
		
		
		
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getValorMercado() {
		return valorMercado;
	}
	public void setValorMercado(int valorMercado) {
		this.valorMercado = valorMercado;
	}
	public boolean isTransferible() {
		return transferible;
	}
	public void setTransferible(boolean transferible) {
		this.transferible = transferible;
	}
	public int getGoles() {
		return goles;
	}
	public void setGoles(int goles) {
		this.goles = goles;
	}
	public int getAsistencias() {
		return asistencias;
	}
	public void setAsistencias(int asistencias) {
		this.asistencias = asistencias;
	}
	public String getPosicion() {
		return posicion;
	}
	public void setPosicion(String posicion) {
		this.posicion = posicion;
	}
	
	public ArrayList<Jugador> getJugadores() {
		return jugadores;
	}
	public void setJugadores(ArrayList<Jugador> jugadores) {
		this.jugadores = jugadores;
	}
	@Override
	public String toString() {
		return "[nombre=" + nombre + ", valorMercado=" + valorMercado + ", transferible=" + transferible
				+ ", goles=" + goles + ", asistencias=" + asistencias + ", posicion=" + posicion + "]";
	}
	
	
	

}
