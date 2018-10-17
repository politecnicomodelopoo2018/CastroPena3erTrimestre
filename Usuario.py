from BD import *
import hashlib
import smtplib


class Usuario(object):

    id = None
    nombre= None
    contraseña = None
    mail = None
    hincha = None

    def crearUsuario(self, nom, con):

        #users = Usuario.getUsuarios()

        self.nombre = nom
        self.contraseña = con



    def setUsuario(self):

        cursor = BD().run("insert into Usuario (idUsuario, Nombre, Contraseña) values (null, '"+self.nombre+"', '"+self.contraseña+"');")

        self.id = cursor.lastrowid

    def updateUsuario(self):

        BD().run("update Usuario set Nombre = '"+self.nombre+"', Contraseña = '"+self.contraseña+"' where idUsuario = '"+str(self.id)+"';")

    def deleteUsuario(self):

        # contadorProde = BD().run("select count(*) from Prode where Usuario_idUsuario = '"+str(self.id)+"';")
        #
        # cont1 = None

        BD().run("delete from Usuario where idUsuario = '" + str(self.id) + "';")

        # for item in contadorProde:
        #     cont1 = item["count(*)"]
        #
        # if cont1 == 0:
        #
        #     BD().run("delete from Usuario where idUsuario = '" + str(self.id) + "';")
        #
        # else:
        #
        #     return False
    @staticmethod
    def setContraseña(contraseña):

        return hashlib.sha256((contraseña).encode('utf-8')).hexdigest()

    @staticmethod
    def getUsuario(unID):

        d = BD().run("Select * from Usuario where idUsuario = '" + str(unID) + "';")
        lista = d.fetchall()
        UnUsuario = Usuario()

        UnUsuario.id = lista[0]["idUsuario"]
        UnUsuario.nombre = lista[0]["Nombre"]
        UnUsuario.contraseña = lista[0]["Contraseña"]


        return UnUsuario

    @staticmethod
    def getUsuarios():

        d = BD().run("Select * from Usuario;")

        lista_aux = []

        for item in d:
            lista_aux.append(item)

        return lista_aux

    @staticmethod
    def getUsuarioPorNombre(username):


        u = BD().run("select * from Usuario where Nombre = '"+username+"';")
        usuario = u.fetchall()
        iduser = usuario[0]["idUsuario"]
        user = Usuario.getUsuario(iduser)

        return user
