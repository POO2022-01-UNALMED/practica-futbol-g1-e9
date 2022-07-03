from gestorAplicacion.organizacion.Arbitro import Arbitro
from gestorAplicacion.organizacion.Liga import Liga
from gestorAplicacion.organizacion.Arbitro import Arbitro
import pathlib
import os
import pickle
#*
# * Se utiliza para serializar todos los objetos creados durante la ejecucion
# * del proyecto
# * @author Sebastian Valencia
# * @author Mateo Canavera
# 

class Serializador:
    #	*
    #	 * Serializamos una lista por el nombre de la clase
    #	 * 
    #	 * @param <E>       el generico se usa para poder agredar las clases que se
    #	 *                  crearon
    #	 * @param lista     Una lista de objetos
    #	 * @param className El nombre de la clase que queremos usar como nombre del
    #	 *                  archivo
    #	 
    class Serializador():
    
        def serializar(lista, className):
            def camino(className):
                string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
                return string
            try:
                # Creo el archivo pickle para guardar los objetos
                picklefile = open(camino(className), 'wb')
                # pickle el objeto en el archivo
                pickle.dump(lista, picklefile)
                # cierro el archivo para guardar
                picklefile.close()
                
            except:
                print("paila tuqui tuqui muñeco")

    def serializarTodo():

        Serializador.serializar(Liga.getEquipos(), "Equipos")
        Serializador.serializar(Liga.getCalendario(), "Calendario")
        Serializador.serializar(Liga.getJugadoresLibres(), "JugadoresLibres")
        Serializador.serializar(Arbitro.federacionArbitros, "Arbitros")

        