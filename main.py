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


Ligue = Liga()
Equipe1 = Equipo()
Equipe2 = Equipo()
Match1 = Partido()

@app.route('/')
def Index():
    return render_template("/menu.html")

@app.route('/laLiga')
def laLiga():
    b = BD().run("select * from Equipo join DatosLiga on DatosLiga.Equipo_idEquipo = Equipo.idEquipo where DatosLiga.Liga_idLiga = 1 order by Puntos DESC;")
    lista = b.fetchall()

    return render_template("/laLiga.html", equiposLaLiga = lista)

@app.route('/superliga')
def Superliga():

    b = BD().run("select * from Equipo join DatosLiga on DatosLiga.Equipo_idEquipo = Equipo.idEquipo where DatosLiga.Liga_idLiga = 2 order by Puntos DESC")

    lista = b.fetchall()

    return render_template("/superliga.html", equiposSuperliga = lista)

@app.route('/libertadores')
def Libertadores():
    return render_template("/libertadores.html")

@app.route('/uefa')
def Uefa():
    return render_template("/uefa.html")




# Ligue.crearLiga("La Liga Santander", "España", None, False, 2018)
#
# Ligue.setLiga()
#
# Equipe1.crearEquipo("Atletico de Madrid", 1, None)
# Equipe2.crearEquipo("Boca Juniors", 1, None)


# Equipe1.setEquipo()
# Equipe2.setEquipo()

# Match1.crearPartido(1, 2, 2, 1, 1, None)

# Match1.setPartido()

# Cup=Copa()

# Cup=Copa.getCopa(2)

# Cup.crearCopa("UEFITA CACA", "UEfafafa", 1, "Terminada")

# Cup.updateCopa()

# Cup.crearCopa("UEFA CAQUITA", "UEFA", None, "Final")

# Cup.setCopa()

# User = Usuario()

# User.crearUsuario("Franckius", "unacontraseñafacil", "francopenaaaaaaaaaaaj2000@yahoo.com", 1)

# User.setUsuario()

# Prode = Prode()

# Prode.crearProde(1,1,3,1)

# Prode.setProde()

# Equipe1.crearEquipo("Futbol Club Barcelona", 3, 2)

# Equipe1.setEquipo()

# Equipe1 = Equipo.getEquipo(2)

# Equipe1.crearEquipo("Real Mandril", 3, 2)

# Equipe1.updateEquipo()

# Match1.crearPartido(2,4,0,7,3,None)

# Match1.setPartido()

# Match1= Partido.getPartido(3)

# Match1.deletePartido()

#print(Prode.getProdes())


if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal


opcion = input("pepe")

while opcion != 8:

    if opcion == 1:

        opcionUno= input("1-ins"
                        "2-del"
                        "3-upt")

        if opcionUno == 1:

            #insertar

        elif opcionUno == 2:

            #deletear

        elif opcionUno == 3:

            #updatear

        else:

            opcion=input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 2:

        opcionDos = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionDos == 1:

            #insertar

        elif opcionDos == 2:

            #deletear

        elif opcionDos == 3:

            #updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 3:

        opcionTres = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionTres == 1:

            # insertar

        elif opcionTres == 2:

            # deletear

        elif opcionTres == 3:

            # updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 4:

        opcionCuatro = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionCuatro == 1:

            # insertar

        elif opcionCuatro == 2:

            # deletear

        elif opcionCuatro == 3:

            # updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 5:

        opcionCinco = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionCinco == 1:

            # insertar

        elif opcionCinco == 2:

            # deletear

        elif opcionCinco == 3:

            # updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 6:

        opcionSix = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionSix == 1:

            # insertar

        elif opcionSix == 2:

            # deletear

        elif opcionSix == 3:

            # updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 7:

        opcionSiete = input("1-ins"
                          "2-del"
                          "3-upt")

        if opcionSiete == 1:

            # insertar

        elif opcionSiete == 2:

            # deletear

        elif opcionSiete == 3:

            # updatear

        else:

            opcion = input("se oprimio una opcion correcta, volviendo al menu")

    elif opcion == 8:

        exit()

    else:

        opcion = input("se oprimio una opcion correcta, volviendo al menu")