from Liga import *
from Copa import *
from Partido import *
from Equipo import *
from Usuario import *
from Prode import *
from BD import *
from flask import *

import pymysql



BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


opcion = str(input("1-Liga\n2-Copa\n3-Equipo\n4-Partido\n5-Salir\nOPCION: "))

Ligue = Liga()
Cope = Copa()
Equipe = Equipo()
User = Usuario()
Match = Partido()


while opcion != "5":

    if opcion == "1":

        opcionUno = str(input("1-ins\n"
                               "2-del\n"
                               "3-upt\n"
                               "4-Volver\n"
                               "OPCION: "))

        if opcionUno == "1":

            nomLig = input("Escriba el nombre de la liga: ")
            paisLig = input("Escriba el pais de la liga: ")
            termLig = input("Termino la liga? (si/no): ")
            while  termLig != "si" and termLig != "no":

                termLig = str(input("Termino la liga? (si/no): "))

            if termLig == "si":

                print(Equipo.getEquipos())

                idEquipe = int(input("Quien fue el campeon? (idEquipo): "))

                Equipe = Equipo.getEquipo(idEquipe)

                while Equipe.liga != Ligue.id:

                    print(Equipo.getEquipos())

                    idEquipe = int(input("El equipo ingresado no pertenece a esa liga, vuelva a intentar: "))

                    Equipe = Equipo.getEquipo(idEquipe)

                campLiga = Equipe.id


            elif termLig == "no":

                campLiga = "null"


            anioLiga = input("Escriba el anio de la liga: ")


            Ligue.crearLiga(nomLig, paisLig, campLiga, termLig, anioLiga)

            Ligue.setLiga()


        elif opcionUno == "2":

            print(Liga.getLigas())

            idLigue = int(input("Escriba el id de la liga: "))

            Ligue = Liga.getLiga(idLigue)

            Ligue.deleteLiga()



        elif opcionUno == "3":

            print(Liga.getLigas())

            idLigue = int(input("Escriba el id de liga que desea modificar: "))

            Ligue = Liga.getLiga(idLigue)

            nomLig = input("Escriba el nombre de la liga: ")
            paisLig = input("Escriba el pais de la liga: ")
            termLig = input("Termino la liga? (si/no): ")
            while termLig != "si" and termLig != "no":
                termLig = input("Termino la liga? (si/no): ")

            if termLig == "si":

                print(Equipo.getEquipos())

                idEquipe = int(input("Quien fue el campeon? (idEquipo): "))

                Equipe = Equipo.getEquipo(idEquipe)

                while Equipe.liga != Ligue.id:

                    print(Equipo.getEquipos())

                    idEquipe = int(input("El equipo ingresado no pertenece a esa liga, vuelva a intentar: "))

                    Equipe = Equipo.getEquipo(idEquipe)


                campLiga = Equipe.id


            elif termLig == "no":

                campLiga = None

            anioLiga = input("Escriba el anio de la liga: ")

            Ligue.crearLiga(nomLig, paisLig, campLiga, termLig, anioLiga)

            Ligue.updateLiga()


        elif opcionUno == "4":

            opcion = input("1-Liga\n2-Copa\n3-Equipo\n4-Partido\n5-Salir\nOPCION: ")

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentar")


    elif opcion == "2":

        opcionDos = str(input("1-ins\n"
                               "2-del\n"
                               "3-upt\n"
                               "4-Equipos a grupos\n"
                               "5-Volver\n"
                               "OPCION: "))

        if opcionDos == "1":

            nomCopa = input("Escriba el nombre de la copa: ")
            OrgCopa = input("Escriba la organizacion de la copa: ")
            insCopa = input("Ingrese la instancia de la copa: ")

            if insCopa == "Terminado":

                print(Equipo.getEquipos())

                idEquipe = int(input("Quien fue el campeon? (idEquipo): "))

                Equipe = Equipo.getEquipo(idEquipe)

                while Equipe.copa != Cope.id:

                    print(Equipo.getEquipos())

                    idEquipe = int(input("El equipo ingresado no pertenece a esa liga, vuelva a intentar: "))

                    Equipe = Equipo.getEquipo(idEquipe)

            campCopa = Equipe.copa

            cantGrup = int(input("Escriba la cantidad de grupos de la copa: "))

            Cope.crearCopa(nomCopa, OrgCopa, campCopa, insCopa, cantGrup)

            Cope.setCopa()


        elif opcionDos == "2":

            print(Copa.getCopas())

            idCope = int(input("Escriba el id de la copa: "))

            Cope = Copa.getCopa(idCope)

            Cope.deleteCopa()


        elif opcionDos == "3":

            print(Copa.getCopas())

            idCope = int(input("Escriba el id de la copa que desea modificar: "))

            Cope = Copa.getCopa(idCope)

            nomCopa = input("Escriba el nombre de la copa: ")
            OrgCopa = input("Escriba la organizacion de la copa: ")
            insCopa = input("Ingrese la instancia de la copa: ")

            if insCopa == "Terminado":

                print(Equipo.getEquipos())

                idEquipe = int(input("Quien fue el campeon? (idEquipo): "))

                Equipe = Equipo.getEquipo(idEquipe)

                while Equipe.copa != Cope.id:

                    print(Equipo.getEquipos())

                    idEquipe = int(input("El equipo ingresado no pertenece a esa liga, vuelva a intentar: "))

                    Equipe = Equipo.getEquipo(idEquipe)

            campCopa = Equipe.copa

            cantGrup = int(input("Escriba la cantidad de grupos de la copa: "))

            Cope.crearCopa(nomCopa, OrgCopa, campCopa, insCopa, cantGrup)

            Cope.updateCopa()


        elif opcionDos == "4":

            print(Copa.getCopas())

            idCopaGr = input("Escriba el id de copa para establecer los grupos: ")

            Cope = Copa.getCopa(idCopaGr)

            Squads = Equipo.getEquipos()

            for eqs in Squads:

                if eqs["Copa_idCopa"] == Cope.id:

                    if eqs["Grupo"] == None:

                        grupoletra = input("Ingrese el Grupo del equipo " + eqs["Nombre"] + " de la copa " + Cope.nombre + " : ")

                        Equipe = Equipo.getEquipo(eqs["idEquipo"])

                        Equipe.crearEquipo(Equipe.nombre,Equipe.liga, Equipe.copa, grupoletra)

                        Equipe.updateEquipo()


        elif opcionDos == "5":

            opcion = input("1-Liga\n2-Copa\n3-Equipo\n4-Partido\n5-Salir\nOPCION: ")


        else:

            print("se oprimio una opcion incorrecta, vuelva a intentar")


    elif opcion == "3":

        opcionTres = str(input("1-ins\n"
                          "2-del\n"
                          "3-upt\n"
                          "4-Volver"
                          "OPCION: "))

        if opcionTres == "1":

            nomEquipo = input("Escriba el nombre del equipo: ")

            print(Liga.getLigas())

            idliga = int(input("Escriba el nro id de la liga a la que pertenece el equipo: "))

            #VERIFICAA FORRO

            juegaCopa = input("Pertenece a una copa? (si/no): ")

            if juegaCopa == "si":

                print(Copa.getCopas())

                idcopa = int(input("Escriba el nro id de la copa a la que pertenece el equipo:"))


            elif juegaCopa == "no":

                idcopa = None

            grupo = "null"

            Equipe.crearEquipo(nomEquipo, idliga, idcopa, grupo)

            Equipe.setEquipo()


        elif opcionTres == "2":

            print(Equipo.getEquipos())

            idEquipoDel = int(input("Escriba el id del equipo que desea eliminar: "))

            Equipe =  Equipo.getEquipo(idEquipoDel)

            Equipe.deleteEquipo()


        elif opcionTres == "3":

            print(Equipo.getEquipos())

            idEquipo = int(input("Escriba el id del equipo que desea modificar: "))

            Equipe = Equipo.getEquipo(idEquipo)

            nomEquipo = input("Escriba el nombre del equipo: ")

            print(Liga.getLigas())

            idliga = int(input("Escriba el nro id de la liga a la que pertenece el equipo: "))

            # VERIFICAA FORRO

            juegaCopa = input("Pertenece a una copa? (si/no): ")
            idcopa= "null"

            if juegaCopa == "si":

                print(Copa.getCopas())

                idcopa = int(input("Escriba el nro id de la copa a la que pertenece el equipo:"))


            if Equipe.grupo != None:

                grupoLet = input("Escriba la letra de grupo de la copa: ")

            grupoLet = "null"

            Equipe.crearEquipo(nomEquipo, idliga, idcopa, grupoLet)

            Equipe.updateEquipo()

        elif opcionTres == "4":

            opcion = input("1-Liga\n2-Copa\n3-Equipo\n4-Partido\n5-Salir\nOPCION: ")

        else:

            print("se oprimio una opcion incorrecta, vuelva a intentar")



    elif opcion == "4":

        opcionCuatro = input("1-ins\n"
                          "2-del\n"
                          "3-upt\n"
                          "4-Volver\n"
                          "OPCION: ")

        if opcionCuatro == "1":

            print(Equipo.getEquipos())

            eq1 = input("Escriba el id del 1er equipo: ")

            eq2 = input("Escriba el id del 2do equipo: ")

            while eq1 == eq2:

                print("los id de los equipos no se pueden repetir, vuelva a intentar: ")

                eq1 = input("Escriba el id del 1er equipo: ")

                eq2 = input("Escriba el id del 2do equipo: ")

            Equipe1 = Equipo.getEquipo(eq1)
            Equipe2 = Equipo.getEquipo(eq2)

            programarPart = input("El partido ya se jugo? (si/no) : ")

            while programarPart != "no" and programarPart != "yes":

                programarPart = input("El partido ya se jugo? (si/no) : ")

            if programarPart == "si":

                goalsEq1 = input("Cuantos goles metio "+Equipe1.nombre+"?: ")
                goalsEq2 = input("Cuantos goles metio "+ Equipe2.nombre + "?: ")

                aQuePertenece = input("Partido es de Liga, Copa o Amistoso?:")

                if aQuePertenece == "Liga":

                    print(Liga.getLigas())

                    idliga = int(input("Ingrese el idLiga a la que pertenece el partido: "))

                    fecha = input("Nro Fecha del partido: ")

                    Match.crearPartido(eq1,eq2,goalsEq1,goalsEq2,idliga,None,fecha,None)

                elif aQuePertenece == "Copa":

                    print(Copa.getCopas())

                    idcopa = input("Ingrese el idCopa a la que pertenece el partido: ")

                    instance= input("Ingrese la Instancia de la Copa (Fase/Octavos/Cuartos/Semis/Final/Terminado): ")

                    while instance != "Fase" and instance != "Octavos" and instance != "Cuartos" and instance != "Semis" and instance != "Final" and instance != "Terminado":

                        instance = input("Se ingreso una instancia incorrecta, vuelva a intentar (Fase/Octavos/Cuartos/Semis/Final/Terminado): ")

                    Match.crearPartido(eq1,eq2,goalsEq1,goalsEq2,None,idcopa,None, instance)

                elif aQuePertenece == "Amistoso":

                    Match.crearPartido(eq1,eq2,goalsEq1,goalsEq2,None,None,None,None)


            else:

                aQuePertenece = input("Partido es de Liga, Copa o Amistoso?:")

                if aQuePertenece == "Liga":

                    print(Liga.getLigas())

                    idliga = int(input("Ingrese el idLiga a la que pertenece el partido: "))

                    fecha = input("Nro Fecha del partido: ")

                    Match.crearPartido(eq1, eq2, None, None, idliga, None, fecha, None)

                elif aQuePertenece == "Copa":

                    print(Copa.getCopas())

                    idcopa = input("Ingrese el idCopa a la que pertenece el partido: ")

                    instance = input("Ingrese la Instancia de la Copa (Fase/Octavos/Cuartos/Semis/Final/Terminado): ")

                    while instance != "Fase" and instance != "Octavos" and instance != "Cuartos" and instance != "Semis" and instance != "Final" and instance != "Terminado":
                        instance = input(
                            "Se ingreso una instancia incorrecta, vuelva a intentar (Fase/Octavos/Cuartos/Semis/Final/Terminado): ")

                    Match.crearPartido(eq1, eq2, None, None, None, idcopa, None, instance)

                elif aQuePertenece == "Amistoso":

                    Match.crearPartido(eq1, eq2, None, None, None, None, None, None)

            Match.setPartido()

        elif opcionCuatro == "2":

            print(Partido.getPartidos())

            idPartidoDel = int(input("Escriba el id del partido que desea eliminar: "))

            Match = Partido.getPartido(idPartidoDel)

            Match.deletePartido()

        elif opcionCuatro == "3":

            print(Partido.getPartidos())

            idPartidoUp =input("Escriba el id del partido que quiere modificar: ")

            Match = Partido.getPartido(idPartidoUp)

            print(Equipo.getEquipos())

            eq1 = input("Escriba el id del 1er equipo: ")

            eq2 = input("Escriba el id del 2do equipo: ")

            while eq1 == eq2:
                print("los id de los equipos no se pueden repetir, vuelva a intentar: ")

                eq1 = input("Escriba el id del 1er equipo: ")

                eq2 = input("Escriba el id del 2do equipo: ")

            Equipe1 = Equipo.getEquipo(eq1)
            Equipe2 = Equipo.getEquipo(eq2)

            goalsEq1 = input("Cuantos goles metio " + Equipe1.nombre + "?: ")
            goalsEq2 = input("Cuantos goles metio " + Equipe2.nombre + "?: ")

            aQuePertenece = input("Partido es de Liga, Copa o Amistoso?:")

            if aQuePertenece == "Liga":

                print(Liga.getLigas())

                idliga = int(input("Ingrese el idLiga a la que pertenece el partido: "))

                fecha = input("Nro Fecha del partido: ")

                Match.crearPartido(eq1, eq2, goalsEq1, goalsEq2, idliga, None, fecha, None)

            elif aQuePertenece == "Copa":

                print(Copa.getCopas())

                idcopa = input("Ingrese el idCopa a la que pertenece el partido: ")

                while instance != "Fase" and instance != "Octavos" and instance != "Cuartos" and instance != "Semis" and instance != "Final" and instance != "Terminado":

                    instance = input("Se ingreso una instancia incorrecta, vuelva a intentar (Fase/Octavos/Cuartos/Semis/Final/Terminado): ")

                Match.crearPartido(eq1, eq2, goalsEq1, goalsEq2, None, idcopa, None, instance)

            elif aQuePertenece == "Amistoso":

                Match.crearPartido(eq1, eq2, goalsEq1, goalsEq2, None, None, None,None)

            Match.updatePartido()

        elif opcionCuatro == "4":

            opcion = input("1-Liga\n2-Copa\n3-Equipo\n8-Salir\nOPCION: ")

        else:

            print("se oprimio una opcion correcta, volviendo al menu")



    # elif opcion == 5:

        # opcionCinco = input("1-ins"
    #                       "2-del"
    #                       "3-upt")
    #
    #     if opcionCinco == 1:
    #
    #         # insertar
    #
    #     elif opcionCinco == 2:
    #
    #         # deletear
    #
    #     elif opcionCinco == 3:
    #
    #         # updatear
    #
    #     else:
    #
    #         print("se oprimio una opcion correcta, volviendo al menu")
    #
    #     opcion = input("1-Liga\n2-Copa\n3-Equipo\n8-Salir\nOPCION: ")
    #
    # elif opcion == 6:
    #
    #     opcionSix = input("1-ins"
    #                       "2-del"
    #                       "3-upt")
    #
    #     if opcionSix == 1:
    #
    #         # insertar
    #
    #     elif opcionSix == 2:
    #
    #         # deletear
    #
    #     elif opcionSix == 3:
    #
    #         # updatear
    #
    #     else:
    #
    #         print("se oprimio una opcion correcta, volviendo al menu")
    #
    #     opcion = input("1-Liga\n2-Copa\n3-Equipo\n8-Salir\nOPCION: ")
    #
    # elif opcion == 7:
    #
    #     opcionSiete = input("1-ins"
    #                       "2-del"
    #                       "3-upt")
    #
    #     if opcionSiete == 1:
    #
    #         # insertar
    #
    #     elif opcionSiete == 2:
    #
    #         # deletear
    #
    #     elif opcionSiete == 3:
    #
    #         # updatear
    #
    #     else:
    #
    #         print("se oprimio una opcion correcta, volviendo al menu")
    #
    #     opcion = input("1-Liga\n2-Copa\n3-Equipo\n8-Salir\nOPCION: ")

    elif opcion == "5":

        exit()

    # else:
    #
    #     print("se oprimio una opcion correcta, volviendo al menu")