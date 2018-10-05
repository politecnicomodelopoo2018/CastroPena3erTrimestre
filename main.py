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

    grupeA = BD().run("Call pito('A');")
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


    lista = z.fetchall()


    return render_template("/libertadores.html", equiposCopaLib = lista, A = listaA, B = listaB, C = listaC, D= listaD, E = listaE, F = listaF, G = listaG, H = listaH)

@app.route('/uefa')
def Uefa():
    return render_template("/uefa.html")

@app.route('/admin')
def administrarPagina():

    teams = BD().run("select * from Equipo;")

    competencia1 = BD().run("select * from Copa;")
    competencia2 = BD().run("select * from Liga;")
    equipos = BD().run("select * from Equipo")

    copas = competencia1.fetchall()
    ligas = competencia2.fetchall()
    teamLista = equipos.fetchall()

    listaEquipos = teams.fetchall()


    return render_template("/admin.html", Equipos = listaEquipos, Cups = copas, Ligues = ligas, Teams = teamLista)

@app.route('/admin2', methods= ['POST','GET'])
def adminPartidos():

    match = Partido()
    eq1 = request.form.get("Eq1")
    eq2 = request.form.get("Eq2")
    golesEq1 = request.form.get("golesEq1")
    golesEq2 = request.form.get("golesEq2")
    competencia = request.form.get("competencia")

    pito = competencia[1]
    letra = competencia[0]

    if letra == 'A':

        match.crearPartido(eq1,eq2,golesEq1, golesEq2, None, None, None, None)

    elif letra == 'l':

        match.crearPartido(int(eq1), int(eq2), golesEq1, golesEq2, int(pito), None, None, None)

    elif letra == 'c':

        match.crearPartido(int(eq1), int(eq2), golesEq1, golesEq2, None, int(pito),None, None)

    match.setPartido()





    return render_template("/admin.html")


# Ligue.crearLiga("La Liga Santander", "España", None, False, 2018)
#
# Ligue.setLiga()
#
# Equipe1.crearEquipo("Atletico de Madrid", 1, None)
# Equipe2.crearEquipo("Boca Juniors", 1, None)

@app.route('/admin2', methods= ['POST','GET'])
def adminEquipos():

    team = Equipo()

    name = request.form.get("Equipo")
    cup = request.form.get("Copa")
    ligue = request.form.get("Liga")

    team.crearEquipo(name,ligue,cup,None)

    team.setEquipo()


    return render_template("/admin.html")

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

