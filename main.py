from Liga import *
from Copa import *
from Partido import *
from Equipo import *
from Usuario import *
from Prode import *
from BD import *

import pymysql



BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")


Ligue = Liga()
Equipe1 = Equipo()
Equipe2 = Equipo()
Match1 = Partido()


#Ligue.crearLiga("SUPERLIGA", "Argentina", None, False, 2018)

#Ligue.setLiga()

#Equipe1.crearEquipo("Argentinos Juniors", 1, None)
#Equipe2.crearEquipo("Boca Juniors", 1, None)


#Equipe1.setEquipo()
#Equipe2.setEquipo()

#Match1.crearPartido(1, 2, 2, 1, 1, None)

#Match1.setPartido()

#Cup=Copa()

#Cup=Copa.getCopa(2)

#Cup.crearCopa("UEFITA CACA", "UEfafafa", 1, "Terminada")

#Cup.updateCopa()

#Cup.crearCopa("UEFA CAQUITA", "UEFA", None, "Final")

#Cup.setCopa()

#User = Usuario()

#User.crearUsuario("Franckius", "unacontraseñafacil", "francopenaaaaaaaaaaaj2000@yahoo.com", 1)

#User.setUsuario()

#Prode = Prode()

#Prode.crearProde(1,1,3,1)

#Prode.setProde()

#Equipe1.crearEquipo("Futbol Club Barcelona", 3, 2)

#Equipe1.setEquipo()

#Equipe1 = Equipo.getEquipo(2)

#Equipe1.crearEquipo("Real Mandril", 3, 2)

#Equipe1.updateEquipo()

#Match1.crearPartido(2,4,0,7,3,None)

#Match1.setPartido()

#Match1= Partido.getPartido(3)

#Match1.deletePartido()

print(Prode.getProdes())