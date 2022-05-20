package programafutbol;

public  abstract class ClubesDeportivos {
	private String nombre;
	private String localidad;
	private String estadisticas;
	
	
	
	@Override
	public boolean equals(Object o) {
		return this.nombre.equals(((ClubesDeportivos)o).nombre);
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getLocalidad() {
		return localidad;
	}
	public void setLocalidad(String localidad) {
		this.localidad = localidad;
	}
	public String getEstadisticas() {
		return estadisticas;
	}
	public void setEstadisticas(String estadisticas) {
		this.estadisticas = estadisticas;
	}
	

}
