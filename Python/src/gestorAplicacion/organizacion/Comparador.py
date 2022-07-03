from gestorAplicacion.juego.EquipoFutbol import EquipoFutbol

class Comparador():

    def comparador(self, t, t1):

        if t.getPuntos() > t1.getPuntos():
            return -1

        else:
            if t.getPuntos()< t1.getPuntos():
                return 1


            else:
                diferenciaGol = t.getGolesAnotados()-t.getGolesRecibidos()

                diferenciaGol1 = t1.getGolesAnotados()-t1.getGolesRecibidos()

                if diferenciaGol> diferenciaGol1:
                    return -1

                else:
                    if diferenciaGol < diferenciaGol1:
                        return 1
                    else:
                        return 0









"""if __name__ == "__main__":
    t = EquipoFutbol("Madrid","Madrid",presupuesto=1200,plantilla=["kaka","marcelo"],entrenador="Carlooo")
    t1 = EquipoFutbol("Barca","Madrid",presupuesto=1200,plantilla=["kaka","marcelo"],entrenador="Piero")
    t.setPuntos=2
    t1.setPuntos=1
    comparadorp=Comparador()
    comparadorp.comparador(t,t1)
    print(comparadorp.comparador(t,t1))
"""















""" if t.getPuntos() > t1.getPuntos():
            return -1

        else:
            if t.getPuntos()< t1.getPuntos():
                return 1

            else:
                diferenciaGol = t.getGolesAnotados()-t.getGolesRecibidos()

                diferenciaGol1 = t1.getGolesAnotados()-t1.getGolesRecibidos()

                if diferenciaGol> diferenciaGol1:
                    return -1

                else:
                    if diferenciaGol < diferenciaGol1:
                        return 1
                    else:
                        return 0
"""






