from gestorAplicacion.juego.EquipoFutbol import EquipoFutbol
from gestorAplicacion.organizacion.Liga import Liga
from gestorAplicacion.juego.ClubDeportivo import ClubDeportivo
from gestorAplicacion.juego.Entrenador  import Entrenador
from gestorAplicacion.juego.IntegranteEquipo import IntegranteEquipo
from gestorAplicacion.organizacion.Arbitro import Arbitro
from gestorAplicacion.organizacion.Comparador import Comparador
from gestorAplicacion.organizacion.Jornada import Jornada
from gestorAplicacion.organizacion.Partido import Partido
from gestorAplicacion.organizacion.PartidoJugado import PartidoJugado
from ui_main.field_frame import FieldFrame
from ui_main.inicio import Inicio
from baseDatos.Serializador import Serializador
from ctypes import resize
from tkinter import *
from numpy import diag
from random import choice, random, randint
from .equipo_inexistente import equipoNoexistenteException

from .error_aplicacion import ErrorAplicacion
from .exception_pop_up import ExceptionPopUp
from .Equipo_incorrecto_exception import EquipoIncorrectoException
from gestorAplicacion.organizacion.Liga import Liga


        

def outPut(string, text):
    text.delete("1.0", "end")
    text.insert(INSERT, string)
    text.pack(fill=X, expand=True)




def iniciar_ventana_usuario():
    #Ventana principal
    window = Tk()
    window.geometry("680x420")
    window.title("Fotball Manager")
    window.option_add("*tearOff",  FALSE)
    #window.iconbitmap('./imagenes/icono.ico')



    #Métodos sin argumentos para poder ejecutarlos-------------------------------------


    framesAMatar = []

    def matarloTodo(frameUtilizado):

        for frame in framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH,expand=True)



    def evtanadirEquipo():
        matarloTodo(equipoManual)

    def evteliminarEquipo():
        matarloTodo(eliminarEquipo)
    
    

    def evtmostrarTabladeLiga():
        matarloTodo()


    outPutGenerarcalendario = Text(window, height=4)
    framesAMatar.append(outPutGenerarcalendario)

    def evtgenerarCalendario():

       arbitros=[Arbitro("Howard Webb", 1200),
                 Arbitro("Pierluigi Collina"),
                 Arbitro("Nestor Pitana"),
                 Arbitro("Felix Brycht")]

        
        
         
        
    
    #Output de mostrar equipos
    outPutMostrarEquipos = Text(window, height=4)
    framesAMatar.append(outPutMostrarEquipos)
    #Evento para mostrar equipos
    def evtMostrarEquipos():
        stri = ""
        for equipo in range(len(Liga.getEquipos())):
            stri+=Liga.getEquipos()[equipo]+"\n"
        if stri == "":
            stri = "Aun no hay ningun Equipo. :("
        elif len(Liga.ligaCompleta) == False:
            equiposFaltantes=Liga.getNumeroDeEquipos-len(Liga.getEquipos(equipo))
            stri="\n" + "Falta anadir " + equiposFaltantes + " equipos a la Liga" + "\n"
        outPut(stri, outPutMostrarEquipos)
        matarloTodo(outPutMostrarEquipos)
    
    
    
    
    #Abre la pestana de dialogo con los nombres de los integrantes del equipo
    def open_popup():
        top= Toplevel(window)
        top.grid_rowconfigure(0, weight=1)
        top.geometry("450x250")
        top.resizable(False,False)
        top.title("Ayuda")
        Label(top, text= "AUTORES\nMateo Cañavera Aluma\nSebastian Valencia Zapata", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

    #Abre la pestana de dialogo con la informacion del programa y su funcionalidad. 
    def aplicacion_popup():
        top= Toplevel(window)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")
        Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
    textonimo = "Football Manager es una compañía administrativa y de espectáculos .\nSe busca crear un programa que emule las interacciones de Football Manager,\npara mejorar la organización de la empresa y proveer un mejor servicio.\nAqui podrás crear tu equipo,generar un calendario de partidos\nemparejarlo con diferentes rivales,consultar la tabla de resultados de los enfrentamientos,\nhasta entrar en un mercado de traspasos para mejorar a tu equipo."




    #----------------------------------------------------------------------------------
    def salir():
        Serializador.serializarTodo()
        from ui_main.ventana_inicio.inicio import VentanaInicio
        framesAMatar = []
        window.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()
        
    def evento():
        pass

    frame_a = Frame()#master = window
    
    frame_a.pack()
    #Barra menu superior
    menubar = Menu()

    menuarchivo = Menu(window)
    menuprocesos = Menu(window)
    menuayuda = Menu(window)
    

    menubar.add_cascade(menu = menuarchivo,
                        label='Archivo',
                        command = evento)
    menubar.add_cascade(menu = menuprocesos,
                        label = 'Procesos y Consultas',
                        command = evento)
    menubar.add_cascade(menu = menuayuda,
                        label='Ayuda',
                        command = evento)

    #submenu de procesos y consultas
    submenu = Menu(window)
    menuprocesos.add_command(label = "Cree un Equipo y anadalo a La Liga", command = evtanadirEquipo)
    menuprocesos.add_command(label = "Eliminar un Equipo de la Liga", command = evteliminarEquipo)
    
    
    
    submenu.add_command(label = "Generar calendario", command = evtgenerarCalendario)
    menuarchivo.add_command(label = "Aplicacion", command = aplicacion_popup)
    menuarchivo.add_command(label = "Guardar y salir", command = salir)
    menuprocesos.add_command(label = "Mostrar Equipos", command =evtMostrarEquipos)
    menuprocesos.add_cascade(label = "Calendario", menu = submenu)
    menuprocesos.add_command(label = "Registrar resultados de jornada", command = evtanadirEquipo)
    menuprocesos.add_command(label = "Mostrar la tabla de la Liga ", command =  evtmostrarTabladeLiga)
    menuprocesos.add_command(label = "Mostrar las estadisticas por Equipo", command = evtanadirEquipo)
    menuprocesos.add_command(label = "Fichar un jugador", command = evtanadirEquipo)

    

    
    

    menuayuda.add_command(label = "Acerca de", command = open_popup)

    window['menu'] = menubar


    #Frame de creacion manual del cliente ------------------------------------------------------------
    window.resizable(True,True)

  



    #Interfaz de inicio----------------------------------------------------------------
    interfazInicio = Inicio(window)

    framesAMatar.append(interfazInicio)
    #----------------------------------------------------------------------------------

    equipoManual = Frame(window, bd=10)
    nombre = Label(equipoManual, text="Crear Equipo", bd= 10)                            
    
    #Frame de anadir un Equipo
    anadirunEquipo = Frame(window)
    descripcion = Label(equipoManual, text="Diligenciar la siguiente información para la correcta creacion del equipo : ", bd= 10)
    crearEquipo = FieldFrame(equipoManual, "Datos Equipo",["Nombre", "Ubicacion", "Presupuesto","Entrenador"], "Valor", [ None, None, None,None],[None],[0, 0, 1, 0])
    crearEquipo.grid_columnconfigure(0, weight=1)
    crearEquipo.grid_columnconfigure(1, weight=1)
    crearEquipo.grid_rowconfigure(0, weight=1)
    crearEquipo.grid_rowconfigure(1, weight=1)
    crearEquipo.grid_rowconfigure(2, weight=1)
    crearEquipo.grid_rowconfigure(3, weight=1)
    crearEquipo.grid_rowconfigure(4, weight=1)
   
    
    output = Text(equipoManual, height=3)
    framesAMatar.append(output)

    
        

    def creacionEquipo():
        try:
            crearEquipo.aceptarCheck()
            
            if Liga.ligaCompleta== True:
        
                outPut("No se puede agregar mas equipos a la Liga",output)
           
            else: 
                 #Falta organizar los otros parametros de los clientes
                Equipo = EquipoFutbol(crearEquipo.getValue("Nombre"), crearEquipo.getValue("Ubicacion"),crearEquipo.getValue("Presupuesto"),crearEquipo.getValue("Entrenador"))
                #Resetear entries del FieldFrame
                crearEquipo.setEntries(list())
                #Refrescar el FieldFrame
                crearEquipo.actualizacion()

                outPut("Se ha creado el Equipo con " + Equipo.__str__(), output)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))
        
    #Creacion de los botones para aceptar y borrar de creacion manual de cliente
    crearEquipo.crearBotones(creacionEquipo)   #     Aceptar             Borrar

    nombre.pack()
    #texto.pack()
    interfazInicio.pack()
    descripcion.pack()
    crearEquipo.pack(fill=BOTH,expand=True)
    framesAMatar.append(equipoManual)

    

    eliminarEquipo = Frame(window)
    nombreEliminarEquipo = Label(eliminarEquipo, text="Eliminar un Equipo", bd=10)
    dcreliminarequipo = Label(eliminarEquipo, text="Ingrese el nombre del equipo que quiere eliminar", bd=10)
    deleteEquipo = FieldFrame(eliminarEquipo, None, ["Nombre Equipo"], None, [None], [],[0])
    outputeliminarEquipo = Text(eliminarEquipo, height=3)
    framesAMatar.append(outputeliminarEquipo)


    def eliminacionequipo():
        try:
            deleteEquipo.aceptarCheck()
            equipochao=deleteEquipo.getValue("Nombre Equipo")
            if Liga.equipoPertenece(equipochao)==True:
                Liga.eliminarEquipo(equipochao)

            outPut(("Se ha Eliminado el equipo:"+ deleteEquipo.getValue("Nombre Equipo")), outputeliminarEquipo) 
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    deleteEquipo.crearBotones(eliminacionequipo)

    nombreEliminarEquipo.pack()
    dcreliminarequipo.pack()
    deleteEquipo.pack()
    framesAMatar.append(eliminarEquipo)
    
    

  
    

    window.mainloop()