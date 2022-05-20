package programafutbol;
import java.util.ArrayList;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Collections;
import java.util.Date;
import java.util.Scanner;



public class Liga extends Equipo {
	private final int numerodeEquipos;
	private final ArrayList<Equipo> liga = new ArrayList<Equipo>();
	private final ArrayList<Partido> partidos= new ArrayList<Partido>();
	
	
	Public Liga(int numerodeEquipos) {
		this.numerodeEquipos=numerodeEquipos;
		liga =new ArrayList<>();
		
	}
	
	public String mostarEstadisticas(){
		for (Equipo equipo:liga) {
			return equipo.getNombre()+"\n"
		+equipo.getVictorias()+"\n"+ 
					
					;
					
		}
		
	}
}
