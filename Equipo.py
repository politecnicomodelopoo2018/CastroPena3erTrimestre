from BD import *

class Equipo(object):

    id = None
    nombre = None
    liga = None
    copa = None
    grupo = None



    def crearEquipo(self, nom, idL, idC, letraGr):

        self.nombre = nom
        self.liga = idL
        self.copa = idC
        self.grupo = letraGr

    def setEquipo(self):

        participarCopa = "null"

        if self.copa is not None:

            participarCopa = self.copa

        if self.grupo is None:

            self.grupo = "Null"

            cursor = BD().run("insert into Equipo (idEquipo, Copa_idCopa, Liga_idLiga, Nombre, Grupo) values (null, "+str(participarCopa)+", '"+str(self.liga)+"', '"+self.nombre+"', "+str(self.grupo)+");")

        elif self.grupo is not None:

            cursor = BD().run("insert into Equipo (idEquipo, Copa_idCopa, Liga_idLiga, Nombre, Grupo) values (null, " + str(participarCopa) + ", '" + str(self.liga) + "', '" + self.nombre + "', '" + str(self.grupo) + "');")

        self.id = cursor.lastrowid


    def updateEquipo(self):

        if self.copa is None:

            self.copa = "null"

        if self.grupo == "null" or self.grupo == "Null":

            BD().run("update Equipo set Nombre = '"+self.nombre+"', Copa_idCopa = "+str(self.copa)+", Liga_idLiga = "+str(self.liga)+", Grupo = "+str(self.grupo)+" where idEquipo = '"+str(self.id)+"';")

        else:

            BD().run("update Equipo set Nombre = '" + self.nombre + "', Copa_idCopa = " + str(self.copa) + ", Liga_idLiga = " + str(self.liga) + ", Grupo = '" + str(self.grupo) + "' where idEquipo = '" + str(self.id) + "';")

    def deleteEquipo(self):



        contadorPartido = BD().run("select count(*) from Partido where idEquipo1 = '"+str(self.id)+"';")
        contadorPartido1 = BD().run("select count(*) from Partido where idEquipo2 = '"+str(self.id)+"';")

        # contadorHinchas = BD().run("select count(*) from Usuario where Equipo_idEquipo = '" + str(self.id) + "';")

        cont1 = None

        for item in contadorPartido:
            cont1 = item["count(*)"]

        cont2 = None

        for item in contadorPartido1:
            cont2 = item["count(*)"]

        # cont3 = None
        #
        # for item in contadorHinchas:
        #
        #     cont3 = item["count(*)"]
        #
        if cont1 == 0 and cont2 == 0:

            BD().run("delete from DatosLiga Where Equipo_idEquipo = '" + str(self.id) + "';")
            BD().run("delete from DatosCopa Where Equipo_idEquipo = '" + str(self.id) + "';")
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
        UnEquipo.grupo = lista[0]["Grupo"]

        return UnEquipo

    @staticmethod
    def getEquipos():

        d = BD().run("Select * from Equipo;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux
