from BD import *


class Liga(object):

    id = None
    nombre = None
    pais = None
    campeon = None
    terminada = None
    anio = None


    def crearLiga(self, nom, country, champs, term, year):


        self.nombre=nom
        self.pais=country

        if champs is None:

            self.campeon = None

        else:

            self.campeon= champs

        if term is False:
            self.terminada = "No terminada"

        elif term is True:
           self.terminada = "Terminada"


        self.anio = year


    def setLiga(self):

        ultimoCampeon="null"

        if self.campeon:

            ultimoCampeon=self.campeon

        cursor=BD().run("Insert into Liga (idLiga, Nombre,Pais, idEquipo_Campeon, Terminada, Año) values(null, '"+self.nombre+"','"+self.pais+"', "+str(ultimoCampeon)+", '"+str(self.terminada)+"', '"+str(self.anio)+"');")
        self.id = cursor.lastrowid

    def updateLiga(self):

        BD().run("update Liga Set Nombre = '"+self.nombre+"', Pais = '"+self.pais+"', idEquipo_Campeon ='"+str(self.campeon)+"', Terminada='"+self.terminada+"', Año = '"+str(self.anio)+"' where idLiga = '"+str(self.id)+"';")


    def deleteLiga(self):

        contadorEquipo = BD().run("select count(*) from Equipo where Liga_idLiga = '"+str(self.id)+"';")

        cont1 = None

        for item in contadorEquipo:

            cont1 = item["count(*)"]

        if cont1 == 0:

            BD().run("delete from Liga where idLiga = '"+str(self.id)+"';")

        else:

            return False


    @staticmethod
    def getLiga(unID):

        d = BD().run("Select * from Liga where idLiga = '" + str(unID) + "';")
        lista = d.fetchall()
        UnLiga = Liga()

        UnLiga.id = lista[0]["idLiga"]
        UnLiga.nombre = lista[0]["Nombre"]
        UnLiga.pais = lista[0]["Pais"]
        UnLiga.terminada = lista[0]["Terminada"]
        UnLiga.campeon = lista[0]["idEquipo_Campeon"]
        UnLiga.anio = lista[0]["Año"]

        return UnLiga

    @staticmethod
    def getLigas():

        d=BD().run("Select * from Liga;")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

        return lista_aux