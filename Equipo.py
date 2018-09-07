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

        participarCopa = "null"

        if self.copa is not None:

            participarCopa = self.copa

        cursor = BD().run("insert into Equipo (idEquipo, Copa_idCopa, Liga_idLiga, Nombre) values (null, "+str(participarCopa)+", '"+str(self.liga)+"', '"+self.nombre+"');")

        self.id = cursor.lastrowid


    def updateEquipo(self):

        if self.copa is None:

            self.copa = "null"


        BD().run("update Equipo set Nombre = '"+self.nombre+"', Copa_idCopa = "+str(self.copa)+", Liga_idLiga = "+str(self.liga)+" where idEquipo = '"+str(self.id)+"';")


    def deleteEquipo(self):

        contadorPartido = BD().run("select count(*) from Partido where Equipo_idEquipo = '"+str(self.id)+"';")

        contadorHinchas = BD().run("select count(*) from Usuario where Equipo_idEquipo = '" + str(self.id) + "';")

        cont1 = None

        for item in contadorPartido:
            cont1 = item["count(*)"]

        cont2 = None

        for item in contadorHinchas:

            cont2 = item["count(*)"]

        if cont1 == 0 and cont2 == 0:

            BD().run("delete from Equipo Where idEquipo = '"+str(self.id)+"';")

            return True

        else:

            return False

    @staticmethod
    def getEquipo(unID):

        d = BD().run("Select * from Equipo where idEquipo = '" + str(unID) + "';")
        lista = d.fetchall()
        UnEquipo = Equipo()

        UnEquipo.id = lista[0]["idEquipo"]
        UnEquipo.nombre = lista[0]["Nombre"]
        UnEquipo.liga = lista[0]["Liga_idLiga"]
        UnEquipo.copa = lista[0]["Copa_idCopa"]

        return UnEquipo

    @staticmethod
    def getEquipos():

        d = BD().run("Select * from Equipo;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux
