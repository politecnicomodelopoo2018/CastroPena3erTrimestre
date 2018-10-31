from BD import *

class Fecha(object):

    Nro = None
    Dia = None
    Horario = None
    EquipoLoc = None
    EquipoVis = None

    def crearFecha(self, nrof, eq1, eq2, day, hour):

        self.Nro = nrof
        self.Dia = day
        self.Horario = hour
        self.EquipoLoc = eq1
        self.EquipoVis = eq2

    def setFecha(self):

        BD().run("insert into fecha (idFecha, Dia, Horario, idEquipo1, idEquipo2) values ("+self.Nro+", '"+self.Dia+"', '"+self.Horario+"', "+self.EquipoLoc+","+self.EquipoVis+");")