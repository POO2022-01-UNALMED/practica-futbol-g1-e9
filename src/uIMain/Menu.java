package uIMain;


import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.Comparador;
import gestorAplicacion.Entrenador;
import gestorAplicacion.EquipoFutbol;
import gestorAplicacion.Jornada;
import gestorAplicacion.Jugador;
import gestorAplicacion.Jugador.Posicion;
import gestorAplicacion.Liga;
import gestorAplicacion.Partido;
import gestorAplicacion.PartidoJugado;

public class Menu {
	
	static Scanner scanner = new Scanner(System.in);

	static Liga liga = new Liga();
	
	public static void main(String[] args) {
		
		//cargar();
		
		
		ArrayList<Jugador> plantilla1 = new ArrayList<Jugador>(Arrays.asList(
				new Jugador("Marc Andre Ter Stegen",Posicion.PT,45000000),
				new Jugador("Gerard Pique",Posicion.DF,5000000),
				new Jugador("Gavi",Posicion.MC,60000000),
				new Jugador("Ansu Fati",Posicion.DL,60000000)
				));
		
		ArrayList<Jugador> plantilla2 = new ArrayList<Jugador>(Arrays.asList(
				new Jugador("Alisson",Posicion.PT,60000000),
				new Jugador("Virgil Van Dijk",Posicion.DF,55000000),
				new Jugador("Fabinho",Posicion.MC,60000000),
				new Jugador("Luis Diaz",Posicion.DL,45000000)
				));
		
		ArrayList<Jugador> plantilla3 = new ArrayList<Jugador>(Arrays.asList(
				new Jugador("Pau Lopez",Posicion.PT,12000000),
				new Jugador("William Saliba",Posicion.DF,30000000),
				new Jugador("Boubacar Kamara",Posicion.MC,25000000),
				new Jugador("Cenguiz Under",Posicion.DL,22000000)
				));
		
		ArrayList<Jugador> plantilla4 = new ArrayList<Jugador>(Arrays.asList(
				new Jugador("Gregor Kobel",Posicion.PT,20000000),
				new Jugador("Manuel Akanji",Posicion.DF,30000000),
				new Jugador("Jude Bellingham",Posicion.MC,75000000),
				new Jugador("Erling Haaland",Posicion.DL,150000000)
				));
		
		Entrenador entrenador1 = new Entrenador("Xavi Hernandez");
		Entrenador entrenador2 = new Entrenador("Jurgen Klopp");
		Entrenador entrenador3 = new Entrenador("Jorge Sampaoli");
		Entrenador entrenador4 = new Entrenador("Edin Terzic");
		
		EquipoFutbol equipo1 = new EquipoFutbol("Barcelona", "Camp Nou"    , 100000000, plantilla1, entrenador1);
		EquipoFutbol equipo2 = new EquipoFutbol("Liverpool", "Anfield"     , 120000000, plantilla2, entrenador2);
		EquipoFutbol equipo3 = new EquipoFutbol("Marsella" , "Velodrome"   , 60000000 , plantilla3, entrenador3);
		EquipoFutbol equipo4 = new EquipoFutbol("Dortmund" , "Signal Iduna", 300000000, plantilla4, entrenador4);
		
		liga.anadirEquipo(equipo1);
		liga.anadirEquipo(equipo2);
		liga.anadirEquipo(equipo3);
		liga.anadirEquipo(equipo4);
		
		boolean salir = false;

		while(!salir) {
			
			System.out.println("----------------------");
			System.out.println("|        Menu De      |");
			System.out.println("|         La Liga     |");
			System.out.println("----------------------");
			System.out.println("");
			System.out.println("Cree un Equipo y anadalo a La Liga (presione 1)");
			System.out.println("Eliminar un Equipo de la Liga (presione 2)");
			System.out.println("Mostrar Equipos (presione 3)");
			System.out.println("");
			System.out.println("Generar calendario (presione 4)");
			System.out.println("Mostrar calendario (presione 5)");
			System.out.println("Designar arbitros y fechas a los enfrentamientos (presione 6)");
			System.out.println("");
			System.out.println("Registrar resultados de jornada (presione 7)");
			System.out.println("Mostrar la tabla de la Liga (presione 8)");
			System.out.println("Mostrar las estadisticas por Equipo (presione 9)");
			System.out.println("");
			System.out.println("Fichar un jugador (presione 10)");
			System.out.println("");
			System.out.println("Salir (presione 11)");
			String linea = scanner.nextLine();
			int comando = 0;
			try {
				comando = Integer.parseInt(linea);
			} catch (Exception e) {
			}
	
			switch(comando) {
			case 1 :
				anadirEquipo();
				break;
			case 2 :
				eliminarEquipo();
				break;
			case 3 :
				mostrarEquipos();
				break;
			case 4:
				generarCalendario();
				break;
			case 5:
				mostrarCalendario();
				break;
			case 6:
				designarArbitrosFechas();
				break;
			case 7 :
				registrarResultadosJornada();
				break;
			case 8:
				mostrarTablaLiga();
				break;
			case 9:
				mostrarEstadisticas();
				break;
			case 10:
				ficharJugador();
				break;
				
			case 11:
				salirDelSistema();
				break;
				
	
	
			default:
				System.out.println("Comando Incorrecto");
	
			}
		}
	
	}
	
	private static void anadirEquipo() {
    	
    	if ( liga.ligaCompleta() ) {
    		System.out.println("No se puede agregar mas equipos a la Liga");
    		return;
    	}
    	EquipoFutbol equipo = new EquipoFutbol();
    	
    	System.out.println("Ingrese el nombre Del equipo");
    	String linea = scanner.nextLine();
    	equipo.setNombre(linea);
    	
    	if ( liga.equipoPertenece(equipo) ) {
    		System.out.println("Este Equipo ya esta en la liga");
    		return;
    	}
    	
    	System.out.println("Ingrese la ubicacion del equipo");
    	linea = scanner.nextLine();
    	equipo.setUbicacion(linea);
    	
    	System.out.println("Ingrese presupuesto del equipo mayor a 0");
    	linea = scanner.nextLine();
    	 
    	 try {
    		 
    		 equipo.setPresupuesto(Integer.parseInt(linea)) ;
         
    	 } catch (Exception e) {
    		 
    		 System.out.println("tienes que ingresar un presupuesto valido");
    		 return;
         
         }
    	 
    	 liga.anadirEquipo(equipo);
    	 
	}
	
	
	private static void eliminarEquipo() {
		System.out.println("Ingrese el nombre del equipo");
		String linea = scanner.nextLine();
		
		EquipoFutbol equipo = liga.identificarEquipo(linea);
		
		if ( liga.equipoPertenece(equipo) ) {
			liga.eliminarEquipo(equipo);
			System.out.println("Equipo " + equipo.getNombre() + " eliminado");
		} else {
			System.out.println("Ese equipo no esta en la liga");
		}
		
	}
	
	
	private static void mostrarEquipos() {
		
		System.out.println("\nEquipos de la Liga: \n");
		
		liga.getEquipos().forEach((equipo) -> {
			System.out.println(equipo.getNombre());
		});
		
		// Si la liga no esta completa
		if (!liga.ligaCompleta()) {
			int equiposFaltantes = liga.getNumeroDeEquipos() - liga.getEquipos().size();
			System.out.println("\n" + "Falta anadir " + equiposFaltantes + " equipos a la Liga" + "\n");
		}
		
	}

	
	private static void generarCalendario() {
		
		// Si la liga aun no tiene fixture y ya fueron agregados todos los equipos
		if ( liga.getCalendario().isEmpty() && liga.ligaCompleta()) {
			
			liga.generarFixture();
			mostrarCalendario();
			
		// Si la liga no esta completa
		} else if (!liga.ligaCompleta()) {
			System.out.println("Faltan equipos por agregar");
			return;
		
		// Si la liga ya tiene fixture
		} else {
			System.out.println("El calendario ya fue creado, no se puede crear nuevamente");
			return;
		}
		
	}

	
	private static void mostrarCalendario() {
		
		List<Jornada> jornadas = liga.getCalendario();
		
		if (jornadas.isEmpty()) {
			
			System.out.println("Aun no se ha generado el Calendario");
			return;
		
		} else {
				
			int indiceJornada = 1;
			
			for (Jornada jornada: jornadas) {
				
				if ( liga.isCalendarioListo() ) {
					System.out.println("\n" + "JORNADA " + indiceJornada + "\n" + jornada.mostrarFecha());
				} else {
					System.out.println("\n" + "JORNADA " + indiceJornada  + "\nFecha por definir");
				}
				
				
				for (Partido partido: jornada.getPartidos()) {
					System.out.println(partido);
				}
				
				System.out.println("");
				indiceJornada++;
				
				}
			
		}
		
	}
	
	
	private static void designarArbitrosFechas() {
		
		if (liga.getCalendario().isEmpty()) {
			System.out.println("El calendario debe ser creado");
			return;
		} else {
			System.out.println("Ingrese la fecha de inicio de la liga: (dd-mm-aaaa)");
			String linea = scanner.nextLine();
			
			Date fechaInicio;
			
	        try {
	        	fechaInicio = new SimpleDateFormat("dd-MM-yyyy").parse(linea);
	        } catch (ParseException ex) {
	            System.out.println("Debes ingresar una fecha valida en formato dd-mm-aaaa");
	            return;
	        }
	        
	        liga.setFechaInicio(fechaInicio);
	        liga.asignarArbitrosFechas();
	        mostrarCalendario();
		}
		
	}
