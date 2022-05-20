package programafutbol;
import java.util.Date;

public class Partido {
	private Equipo equipoA;
	private Equipo equipoB;
	
	private int equipoAmarcador;
	private int equipoBmarcador;
	private Date date;
	public Equipo getEquipoA() {
		return equipoA;
	}
	public void setEquipoA(Equipo equipoA) {
		this.equipoA = equipoA;
	}
	public Equipo getEquipoB() {
		return equipoB;
	}
	public void setEquipoB(Equipo equipoB) {
		this.equipoB = equipoB;
	}
	public int getEquipoAmarcador() {
		return equipoAmarcador;
	}
	public void setEquipoAmarcador(int equipoAmarcador) {
		this.equipoAmarcador = equipoAmarcador;
	}
	public int getEquipoBmarcador() {
		return equipoBmarcador;
	}
	public void setEquipoBmarcador(int equipoBmarcador) {
		this.equipoBmarcador = equipoBmarcador;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	
	
	

}
