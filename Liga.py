from BD import *


class Liga(object):

    id = None
    nombre = None
    pais = None
    campeon = None
    terminada = None


    def crearLiga(self, nom, country, champs, term):

        self.nombre=nom
        self.pais=country
        self.campeon=champs
        self.terminada=term

    def setLiga(self):

        cursor=BD().run("Insert into Liga (idLiga, Nombre,Pais, Campeon, Terminada) values(null, '"+self.nombre+"','"+self.pais+"', '"+str(self.campeon)+"', '"+self.terminada+"');")
        self.id = cursor.lastrowid

    def updateLiga(self):

        BD().run("update Liga Set Nombre = '"+self.nombre+"', Pais = '"+self.pais+"', Campeon ='"+str(self.campeon)+"', Terminada='"+self.terminada+"' where idLiga = '"+str(self.id)+"';")


    def deleteLiga(self):

        contadorEquipo = BD().run("select count(*) from Equipo where Liga_idLiga = '"+str(self.id)+"';")

        cont1 = None

        for item in contadorEquipo:

            cont1 = item["count(*)"]

        if cont1 == 0:

            BD().run("delete from Liga where idLiga = '"+str(self.id)+"';")

        else:

            print("No se puede eliminar la Liga tiene Equipos Asociados a ella")



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


        return UnLiga

    @staticmethod
    def getLigas():

        d=BD().run("Select * from Liga;")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

        return lista_aux