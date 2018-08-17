from BD import *

class Equipo(object):

    id = None
    nombre = None
    liga = None
    copa = None


    def crearEquipo(self, nom, idL, idC):

        self.nombre = nom
        self.liga = idL
        self.copa = idC

    def setEquipo(self):

        cursor = BD().run("insert into Equipo (idEquipo, Copa_idCopa, Equipo_idEquipo, Nombre) values (null, '"+str(self.liga)+"', '"+str(self.copa)+"', '"+self.nombre+"');")

        self.id = cursor.lastrowid

