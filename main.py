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


Ligue.crearLiga("SUPERLIGA", "Argentina", None, False, 2018)

Equipe1.crearEquipo("Argentinos Juniors", 1, None)
Equipe2.crearEquipo("Boca Juniors", 1, None)

Match1.crearPartido(1,2,2,1,1,None)