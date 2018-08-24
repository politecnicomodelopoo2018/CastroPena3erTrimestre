from BD import *

class Prode(object):

    id = None
    partido = None
    usuario = None
    golesEquipo1= None
    golesEquipo2=None


    def crearProde(self, idPartido, user, goalsEq1, goalsEq2):

        self.partido = idPartido
        self.usuario = user
        self.golesEquipo1 = goalsEq1
        self.golesEquipo2 = goalsEq2

    def setProde(self):

        cursor = BD().run("insert into Prode (idProde, Usuario_idUsuario, GolesEquipo1, GolesEquipo2, Partido_idPartidos) values (null,'"+str(self.usuario)+"', '"+str(self.golesEquipo1)+"', '"+str(self.golesEquipo2)+"', '"+str(self.partido)+"' );")

        self.id = cursor.lastrowid

    def updateProde(self):

        BD().run("update Prode set Usuario_idUsuario = '"+str(self.usuario)+"', GolesEquipo1 = '"+str(self.golesEquipo1)+"', GolesEquipo2 = '"+str(self.golesEquipo2)+"', Partido_idPartidos = '"+str(self.partido)+"' where idProde = '"+str(self.id)+"' ;")

    def deleteProde(self):

        BD().run("delete from Prode where idProde ='"+str(self.id)+"'; ")

    @staticmethod
    def getProde(unID):
        d = BD().run("Select * from Prode where idProde = '" + str(unID) + "';")
        lista = d.fetchall()
        UnProde = Prode()

        UnProde.id = lista[0]["idProde"]
        UnProde.Partido = lista[0]["Partido_idPartidos"]
        UnProde.golesEquipo1 = lista[0]["GolesEquipo1"]
        UnProde.golesEquipo2 = lista[0]["GolesEquipo2"]
        UnProde.usuario = lista[0]["Usuario_idUsuario"]

        return UnProde

    @staticmethod
    def getProdes():
        d = BD().run("Select * from Prode;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux
