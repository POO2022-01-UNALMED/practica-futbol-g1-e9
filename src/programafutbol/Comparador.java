package programafutbol;

import java.util.Comparator;

public class Comparador implements Comparator<Equipo> {
	
@Override
public int compare(Equipo t,Equipo t1) {
	
	if(t.getPuntos()> t1.getPuntos())
		return -1;
		
	else
		if (t.getPuntos() < t1.getPuntos())
			return 1;
		else {
			int diferenciagoles=t.getGolesanotados()-t.getGolesrecibidos();
			int diferenciagoles1=t1.getGolesanotados()-t1.getGolesrecibidos();
			
			if (diferenciagoles>diferenciagoles1)
				return -1;
			
			else 
				if (diferenciagoles<diferenciagoles1)
					return 1;
				else return 0;
			
			
		}

}
	
	
	
	
	
	
	

}
