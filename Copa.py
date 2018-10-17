from BD import BD

class Copa(object):

    id = None
    nombre = None
    organizador = None
    campeon = None
    instancia = None
    cantidadGrupos = None


    def crearCopa(self,nom,org,cam,ins, cantGrup):

        if cantGrup is None:

            cantGrup = 8

        if ins is None:

            ins = "Fase"

        if cam is None:

            cam = "Null"


        self.nombre = nom
        self.organizador=org
        self.campeon=cam
        self.instancia=ins
        self.CantidadGrupos = cantGrup

    def setCopa(self):

        hayCampeon = "null"

        if self.campeon:

            hayCampeon = self.campeon

        cursor = BD().run("insert into Copa(idCopa, Nombre, Organizador, idEquipo_Campeon, Instancia, Cant_Grupos) values(null, '"+self.nombre+"', '"+self.organizador+"', "+hayCampeon+", '"+self.instancia+"', '"+str(self.CantidadGrupos)+"');")
        self.id = cursor.lastrowid

    def updateCopa(self):

        if self.campeon is None:

            self.campeon = "null"


        BD().run("update Copa set Nombre = '"+self.nombre+"', Organizador = '"+self.organizador+"', idEquipo_Campeon = "+str(self.campeon)+", Instancia = '"+self.instancia+"', Cant_Grupos = "+str(self.CantidadGrupos)+" where idCopa = '"+str(self.id)+"';")

    def deleteCopa(self):

        contadorEquipo = BD().run("select count(*) from Equipo where Copa_idCopa = '" + str(self.id) + "';")

        cont1 = None

        for item in contadorEquipo:
            cont1 = item["count(*)"]

        if cont1 == 0:

            BD().run("delete from Copa where idCopa = '" + str(self.id) + "';")

        else:

            return False



    @staticmethod
    def getCopa(unID):

        d = BD().run("Select * from Copa where idCopa = '" + str(unID) + "';")
        lista = d.fetchall()
        UnCopa = Copa()

        UnCopa.id = lista[0]["idCopa"]
        UnCopa.nombre = lista[0]["Nombre"]
        UnCopa.organizador = lista[0]["Organizador"]
        UnCopa.campeon = lista[0]["idEquipo_Campeon"]
        UnCopa.instancia = lista[0]["Instancia"]
        UnCopa.CantidadGrupos = lista[0]["Cant_Grupos"]


        return UnCopa

    @staticmethod
    def getCopas():

        d = BD().run("Select * from Copa;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux