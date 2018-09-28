from Liga import *
from Copa import *
from Partido import *
from Equipo import *
from Usuario import *
from Prode import *
from datosCopa import *
from BD import *
from flask import *


import pymysql



BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




@app.route('/')
def Index():
    return render_template("/menu.html")

@app.route('/laLiga')
def laLiga():
    b = BD().run("select * from Equipo join DatosLiga on DatosLiga.Equipo_idEquipo = Equipo.idEquipo where DatosLiga.Liga_idLiga = 2 order by Puntos DESC;")
    lista = b.fetchall()

    return render_template("/laLiga.html", equiposLaLiga = lista)

@app.route('/superliga')
def Superliga():

    b = BD().run("select * from Equipo join DatosLiga on DatosLiga.Equipo_idEquipo = Equipo.idEquipo where DatosLiga.Liga_idLiga = 1 order by Puntos DESC")

    lista = b.fetchall()

    return render_template("/superliga.html", equiposSuperliga = lista)

@app.route('/libertadores')
def Libertadores():

    z = BD().run("select * from Equipo join DatosCopa on DatosCopa.Equipo_idEquipo = Equipo.idEquipo where DatosCopa.Copa_idCopa = 1 order by Puntos DESC")

    grupeA = BD().run("call pito('A');")
    grupeB = BD().run("Call pito('B');")
    grupeC = BD().run("Call pito('C');")
    grupeD = BD().run("Call pito('D');")
    grupeE = BD().run("Call pito('E');")
    grupeF = BD().run("Call pito('F');")
    grupeG = BD().run("Call pito('G');")
    grupeH = BD().run("Call pito('H');")

    listaA = grupeA.fetchall()
    listaB = grupeB.fetchall()
    listaC = grupeC.fetchall()
    listaD = grupeD.fetchall()
    listaE = grupeE.fetchall()
    listaF = grupeF.fetchall()
    listaG = grupeG.fetchall()
    listaH = grupeH.fetchall()

    listaPrimeros= []

    for item in range(2):

        listaPrimeros.append(listaA[item-1])
        listaPrimeros.append(listaB[item-1])
        # listaPrimeros.append(listaC[item-1])
        # listaPrimeros.append(listaD[item-1])
        # listaPrimeros.append(listaF[item-1])
        # listaPrimeros.append(listaG[item-1])
        # listaPrimeros.append(listaH[item-1])



    lista = z.fetchall()



    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []


    for item in lista:


        if item["Grupo"] == 'A':

            lista1.append(item)

        elif item["Grupo"] == 'B':

            lista2.append(item)

        elif item["Grupo"] == 'C':
            lista3.append(item)

        elif item["Grupo"] == 'D':
            lista4.append(item)


        elif item["Grupo"] == 'E':
            lista5.append(item)


        elif item["Grupo"] == 'F':
            lista6.append(item)


        elif item["Grupo"] == 'G':
            lista7.append(item)


        elif item["Grupo"] == "H":
            lista8.append(item)


    return render_template("/libertadores.html", equiposCopaLib = lista, listaA = lista1, listaB= lista2, listaC = lista3, listaD = lista4, listaE = lista5, listaF=lista6, listaG=lista7,listaH=lista8, A = listaA, B = listaB, C = listaC, D= listaD, E = listaE, F = listaF, G = listaG, H = listaH)

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

