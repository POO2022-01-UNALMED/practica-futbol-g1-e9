from gestorAplicacion import Arbitro
from gestorAplicacion.organizacion.Liga import Liga
from gestorAplicacion.organizacion.Arbitro import Arbitro
import pathlib
import os
import pickle
"""
/**
 * Clase para deserializar los objetos que se crearon en ejecucion
 * @author Erik Gonzalez
 * @author Felipe Miranda
 * @author Esteban Garcia
 * @author Emilio Porras 
 */"""


class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo():
       
        Deserializador.deserializar(Liga.getEquipos(), "Equipos")
        Deserializador.deserializar(Liga.getCalendario(), "Calendario")
        Deserializador.deserializar(Liga.getJugadoresLibres(), "JugadoresLibres")
        Deserializador.deserializar(Arbitro.federacionArbitros, "Arbitros")


        #Esta gente guarda en variables los deserializadoss