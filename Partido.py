from BD import *

class Partido(object):

    id = None
    Equipo1 = None
    Equipo2 = None
    GolesEquipo1 = None
    GolesEquipo2 = None
    Liga = None
    Copa = None
    Fecha = None
    Instancia = None
    Dia = None
    Horario = None



    def crearPartido(self,team1, team2, goal1,goal2,ligue,cup,ins,fech, day, hour):

        if team1 == team2:

            return False

        self.Equipo1 = team1
        self.Equipo2 = team2
        self.GolesEquipo1 = goal1
        self.GolesEquipo2 = goal2
        self.Fecha = fech
        self.Dia =day
        self.Horario = hour

        if ligue is None and cup is not None:

            self.Liga = "Null"
            self.Copa = cup
            self.Fecha = "Null"
            self.Instancia = ins

        elif cup is None and ligue is not None:

            self.Liga = ligue
            self.Copa = "Null"
            self.Fecha = fech
            self.Instancia = "Null"

        else:
            self.Liga = "Null"
            self.Copa = "Null"
            self.Fecha = "Null"
            self.Instancia = "Null"



    def setPartido(self):

        if self.Copa is None and self.Liga is None:

            esLiga = "null"
            esCopa = "null"

            self.Liga = esLiga
            self.Copa = esCopa

        elif self.Copa is None:

            esCopa = "null"

            self.Copa = esCopa

        elif self.Liga is None:

            esLiga = "null"

            self.Liga = esLiga

        if self.Instancia is None:

            self.Instancia = "null"

        if self.Fecha is None:

            self.Fecha = "null"

        if self.GolesEquipo1 != "Null" and self.GolesEquipo2 != "Null":

            self.Horario = "Finalizado"


        cursor = BD().run("insert into Partido (idPartidos, idEquipo1, idEquipo2, GolesEquipo1, GolesEquipo2, Liga_idLiga, Copa_idCopa, Instancia, NroFecha, Dia, Horario) values (null, '"+str(self.Equipo1)+"','"+str(self.Equipo2)+"', "+(self.GolesEquipo1)+","+(self.GolesEquipo2)+","+str(self.Liga)+", "+str(self.Copa)+",'"+self.Instancia+"', "+str(self.Fecha)+", '"+str(self.Dia)+"', '"+str(self.Horario)+"');")

        self.id = cursor.lastrowid

    def updatePartido(self):

        if self.Copa is None and self.Liga is None:

            esLiga = "null"
            esCopa = "null"

            self.Liga = esLiga
            self.Copa = esCopa

        elif self.Copa is None:

            esCopa = "null"

            self.Copa = esCopa

        elif self.Liga is None:

            esLiga = "null"

            self.Liga = esLiga
        if self.Instancia is None:

            self.Instancia = "null"

        if self.GolesEquipo1 != "Null" and self.GolesEquipo2 != "Null":

            self.Horario= "Finalizado"



        BD().run("update Partido set idEquipo1 = '"+str(self.Equipo1)+"',idEquipo2 = '"+str(self.Equipo2)+"', GolesEquipo1 = "+self.GolesEquipo1+",GolesEquipo2 = "+self.GolesEquipo2+", Copa_idCopa = "+str(self.Copa)+", Liga_idLiga = "+str(self.Liga)+", NroFecha = "+str(self.Fecha)+", Dia = '"+str(self.Dia)+"', Horario= '"+str(self.Horario)+"', Instancia = '"+self.Instancia+"' where idPartidos = '"+str(self.id)+"';")

    def deletePartido(self):

        #contadorProde = BD().run("select count(*) from Prode where Partido_idPartidos = '"+str(self.id)+"';")

        # cont1 = None
        #
        # for item in contadorProde:
        #
        #     cont1 = item["count(*)"]
        #
        # if cont1 == 0:

        BD().run("delete from Partido where idPartidos = '"+str(self.id)+"';")

        # else:
        #
        #     return False

    @staticmethod
    def getPartido(unID):

        d = BD().run("Select * from Partido where idPartidos = '" + str(unID) + "';")
        lista = d.fetchall()
        UnPartido = Partido()

        UnPartido.id = lista[0]["idPartidos"]
        UnPartido.Equipo1 = lista[0]["idEquipo1"]
        UnPartido.Equipo2 = lista[0]["idEquipo2"]
        UnPartido.Liga = lista[0]["Liga_idLiga"]
        UnPartido.Copa = lista[0]["Copa_idCopa"]
        UnPartido.GolesEquipo1 = lista[0]["GolesEquipo1"]
        UnPartido.GolesEquipo1 = lista[0]["GolesEquipo2"]
        UnPartido.Fecha = lista[0]["NroFecha"]



        return UnPartido

    @staticmethod
    def getPartidos():

        d = BD().run("Select * from Partido;")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux
