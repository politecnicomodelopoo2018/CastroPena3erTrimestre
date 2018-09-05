from BD import BD

class Copa(object):

    id = None
    nombre = None
    organizador = None
    campeon = None
    instancia = None


    def crearCopa(self,nom,org,cam,ins):

        self.nombre = nom
        self.organizador=org
        self.campeon=cam
        self.instancia=ins

    def setCopa(self):

        hayCampeon = "null"

        if self.campeon:

            hayCampeon = self.campeon

        cursor = BD().run("insert into Copa(idCopa, Nombre, Organizador, idEquipo_Campeon, Instancia) values(null, '"+self.nombre+"', '"+self.organizador+"', "+hayCampeon+", '"+self.instancia+"');")
        self.id = cursor.lastrowid

    def updateCopa(self):

        BD().run("update Copa set Nombre = '"+self.nombre+"', Organizador = '"+self.organizador+"', idEquipo_Campeon = '"+str(self.campeon)+"', Instancia = '"+self.instancia+"' where idCopa = '"+str(self.id)+"';")

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

        return UnCopa

    @staticmethod
    def getCopas():

        d = BD().run("Select * from Copa;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux