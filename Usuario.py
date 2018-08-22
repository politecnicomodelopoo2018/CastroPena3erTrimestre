import BD

class Usuario(object):

    id = None
    nombre= None
    contraseña = None
    mail = None
    hincha = None

    def crearUsuario(self, nom, con, meil, equ):

        self.nombre=nom
        self.contraseña=con
        self.mail=meil
        self.hincha=equ


    def setUsuario(self):

        cursor = BD().run("insert into Usuario (idUsuario, Nombre, Contraseña, Mail, Equipo_idEquipo) values (null, '"+self.nombre+"', '"+self.contraseña+"','"+self.mail+"', '"+str(self.hincha)+"');")

        self.id = cursor.lastrowid

    def updateUsuario(self):

        BD().run("update Usuario set Nombre = '"+self.nombre+"', Contraseña = '"+self.contraseña+"', Mail = '"+self.mail+"', Equipo_idEquipo = '"+str(self.hincha)+"' where idUsuario = '"+str(self.id)+"';")

    def deleteUsuario(self):

        contadorProde = BD().run("select count(*) from Prode where Usuario_idUsuario = '"+str(self.id)+"';")

        cont1 = None

        for item in contadorProde:
            cont1 = item["count(*)"]

        if cont1 == 0:

            BD().run("delete from Usuario where idUsuario = '" + str(self.id) + "';")

        else:

            return False

    @staticmethod
    def getUsuario(unID):

        d = BD().run("Select * from Usuario where idUsuario = '" + str(unID) + "';")
        lista = d.fetchall()
        UnUsuario = Usuario()

        UnUsuario.id = lista[0]["idUsuario"]
        UnUsuario.nombre = lista[0]["Nombre"]
        UnUsuario.contraseña = lista[0]["Contraseña"]
        UnUsuario.mail = lista[0]["Mail"]
        UnUsuario.hincha = lista[0]["Equipo_idEquipo"]

        return UnUsuario

    @staticmethod
    def getUsuario():

        d = BD().run("Select * from Usuario;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux
