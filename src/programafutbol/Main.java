package programafutbol;

public class Main {
	public static void main(String[] args) {
		
		Jugador a= new Jugador("Mateo",2000,true,4,22,"Defensa");
		System.out.println(a.getJugadores());
		System.out.println(a.jugadores.size());
		
		Tecnico b=new Tecnico("Ernesto");
		System.out.println(b.ficharJugadores("Defensa", 2000));
		
				
	}
	
	

}
