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



@app.route('/login', methods=['GET','POST'])
def login1():
    if 'username' in session:
        return redirect("/admin")

    userMal = request.args.get("error")
    return render_template("/login.html", error1=userMal)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect('/')


@app.route('/login1', methods=['GET','POST'])
def loginAdmin():

    #submit = request.form.get("Enviar")
    username = request.form.get("nick")
    password = request.form.get("pass")

    try:

        User = Usuario.getUsuarioPorNombre(username)

        password1 = User.setContraseña(password)

        if User.nombre == username and User.contraseña == password1:
            session['username'] = username
            return redirect("/admin")

        else:

            return redirect("/login?error=1")

    except:

        return redirect("/login?error=1")

        # teams = BD().run("select * from Equipo;")
        # matchs = BD().run("select * from Partido;")
        # competencia1 = BD().run("select * from Copa;")
        # competencia2 = BD().run("select * from Liga;")
        # equipos = BD().run("select * from Equipo")
        # usuarios = BD().run("select * from Usuario")
        #
        # copas = competencia1.fetchall()
        # ligas = competencia2.fetchall()
        # teamLista = equipos.fetchall()
        # users = usuarios.fetchall()
        # listaEquipos = teams.fetchall()
        #
        # return render_template("/admin.html", Equipos=listaEquipos, Cups=copas, Ligues=ligas, Teams=teamLista,Partidos=matchs, Usuarios = users)





@app.route('/signUp', methods=['GET', 'POST'])
def signUpAdmin():

    # submit = request.form.get("Enviar")
    username = request.form.get("nick")
    password = request.form.get("pass")

    User = Usuario()

    User.crearUsuario(username, Usuario.setContraseña(password))

    User.setUsuario()

    teams = BD().run("select * from Equipo;")
    matchs = BD().run("select * from Partido;")
    competencia1 = BD().run("select * from Copa;")
    competencia2 = BD().run("select * from Liga;")
    equipos = BD().run("select * from Equipo")
    usuarios = BD().run("select * from Usuario")

    copas = competencia1.fetchall()
    ligas = competencia2.fetchall()
    teamLista = equipos.fetchall()
    users = usuarios.fetchall()
    listaEquipos = teams.fetchall()

    return render_template("/admin.html", Equipos = listaEquipos, Cups = copas, Ligues = ligas, Teams = teamLista, Partidos = matchs, Usuarios = users)


@app.route('/pepe', methods=['POST', 'GET'])
def logInOSignUp():

    return render_template("/login.html")


@app.route('/admin', methods=['POST', 'GET'])
def administrarPagina():
    if not 'username' in session:
        return redirect("/login")


    submit = request.form.get("enviar")
    idpartido = request.form.get("idPartido")
    idequipo = request.form.get("idEquipo")
    idliga = request.form.get("idLiga")
    idcup = request.form.get("idCopa")
    idusuario = request.form.get("idUsuario")

    if submit == "Submit1":
        match = Partido()
        eq1 = request.form.get("Eq1")
        eq2 = request.form.get("Eq2")
        golesEq1 = request.form.get("golesEq1")
        golesEq2 = request.form.get("golesEq2")
        competencia = request.form.get("competencia")

        pito = competencia[1]
        letra = competencia[0]

        if letra == 'A':

            match.crearPartido(eq1, eq2, golesEq1, golesEq2, None, None, None, None)

        elif letra == 'l':

            match.crearPartido(int(eq1), int(eq2), golesEq1, golesEq2, int(pito), None, None, None)

        elif letra == 'c':

            match.crearPartido(int(eq1), int(eq2), golesEq1, golesEq2, None, int(pito), None, None)

        match.setPartido()

    elif submit == "Submit2":

        team = Equipo()

        name = request.form.get("Equipo")
        cup = request.form.get("Copa")
        ligue = request.form.get("Liga")
        grupe = request.form.get("Grupo")

        if grupe == "Null":

            grupe = None

        team.crearEquipo(name, ligue, cup, grupe)

        team.setEquipo()

    elif submit == "Submit3":

        lig = Liga()

        name = request.form.get("nomLiga")
        anio = request.form.get("Año")
        pais = request.form.get("Pais")
        term = request.form.get("term")

        lig.crearLiga(name, pais, None, term, anio)

        lig.setLiga()

    elif submit == "Submit4":

        copa = Copa()

        name = request.form.get("nomCopa")
        org = request.form.get("nomOrg")

        copa.crearCopa(name, org, None, None, None)
        copa.setCopa()

    elif submit == "Submit5":

        user = Usuario()

        username = request.form.get("user")
        password = request.form.get("pass")

        user.crearUsuario(username,Usuario.setContraseña(password))
        user.setUsuario()

    elif submit == "Modificar":

        Match = Partido.getPartido(idpartido)

        team1 = request.form.get("idTeam1")
        team2 = request.form.get("idTeam2")
        golEq1 = request.form.get("golesEq1")
        golEq2 = request.form.get("golesEq2")

        competencia = request.form.get("competencia")

        pito = competencia[1]
        letra = competencia[0]

        if letra == 'A':

            Match.crearPartido(int(team1), int(team2), golEq1, golEq2, None, None, None, None)

        elif letra == 'l':

            Match.crearPartido(int(team1), int(team2), golEq1, golEq2, int(pito), None, None, None)

        elif letra == 'c':

            Match.crearPartido(int(team1), int(team2), golEq1, golEq2, None, int(pito), None, None)

        Match.updatePartido()

    elif submit == "Borrar":

        partidu = Partido.getPartido(idpartido)
        partidu.deletePartido()

    elif submit == "Modificar1":

        Team = Equipo.getEquipo(idequipo)

        nomTeam = request.form.get("nameTeam")
        copaTeam = request.form.get("copaTeam")
        ligaTeam = request.form.get("ligaTeam")
        grupeTeam = request.form.get("teamGrupo")

        Team.crearEquipo(nomTeam, ligaTeam, copaTeam, grupeTeam)

        Team.updateEquipo()

    elif submit == "Borrar1":

        Team = Equipo.getEquipo(idequipo)

        Team.deleteEquipo()

    elif submit == "Modificar2":

        Lig = Liga.getLiga(idliga)

        nomLig = request.form.get("nameLiga")
        anioLig = request.form.get("Año")
        paisLig = request.form.get("Pais")
        termLig = request.form.get("term")


        Lig.crearLiga(nomLig, paisLig, None,termLig,anioLig)

        Lig.updateLiga()

    elif submit == "Borrar2":

        Lig = Liga.getLiga(idliga)

        Lig.deleteLiga()

    elif submit == "Modificar3":

        Cup = Copa.getCopa(idcup)

        nomCup = request.form.get("nameCup")
        orgCup = request.form.get("orgCup")

        Cup.crearCopa(nomCup,orgCup, None, None, None)

        Cup.updateCopa()

    elif submit == "Borrar3":

        Cup = Copa.getCopa(idcup)

        Cup.deleteCopa()

    elif submit == "Modificar4":

        User = Usuario.getUsuario(idusuario)

        nomUs = request.form.get("user")
        contUs = request.form.get("pass")

        contra = Usuario.setContraseña(contUs)

        User.crearUsuario(nomUs, contra)
        User.updateUsuario()

    elif submit == "Borrar4":

        User = Usuario.getUsuario(idusuario)

        User.deleteUsuario()


    teams = BD().run("select * from Equipo;")
    matchs = BD().run("select * from Partido;")
    competencia1 = BD().run("select * from Copa;")
    competencia2 = BD().run("select * from Liga;")
    equipos = BD().run("select * from Equipo;")
    usuarios = BD().run("select * from Usuario;")

    copas = competencia1.fetchall()
    ligas = competencia2.fetchall()
    teamLista = equipos.fetchall()
    listaEquipos = teams.fetchall()
    users = usuarios.fetchall()


    return render_template("/admin.html", Equipos = listaEquipos, Cups = copas, Ligues = ligas, Teams = teamLista, Partidos = matchs, Usuarios = users)




if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
     app.run(debug=True) # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal

