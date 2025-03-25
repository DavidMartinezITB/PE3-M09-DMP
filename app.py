from flask import Flask, render_template, request, redirect, url_for
from utils import validName, validarNombreFichero
from gestio_participants import carregar_participants_de_fitxer, afegir_participant, desar_participants_a_fitxer, eliminarParticipantes, obtenerSaves, cargarParticipantes
import gestio_partides
import puntuacions

# Inicialització de l'aplicació Flask
app = Flask(__name__)

# Ruta de la landing page
@app.route('/')
def home():
    return render_template('index.html')

# Ruta de la gestion de participantes
@app.route('/participants', methods=['GET', 'POST'])
def reqParticipantes():
    # Si la peticion es por GET
    if request.method == 'GET':
        # Cargamos los participantes del fichero predeterminado
        participantes = carregar_participants_de_fitxer()
        # Renderizamos la plantilla pasandole los participantes como parametro
        return render_template('participants.html', participantes=participantes, archivos=obtenerSaves())
    # Si la peticion es por POST -> Envio por formulario
    elif request.method == 'POST':
        # Obtenemos el nombre pasado como parametro POST por formulario
        nombre = request.form.get('nom')
        # Validamos que el nombre cumpla con los requisitos -> REGEX
        if not validName(nombre):
            return '''
            <h1>Nombre no valido</h1>
            <p>Solo puede contener letras y espacios!</p>
            '''
        # Agregamos el participante y si la funcion falla, devolvemos mensaje de error
        if not afegir_participant(nombre):
            return '<h1>ERROR AL CARGAR PARTICIPANTE</h1>'
        # Si la funcion no falla, ha guardado bien el fichero, por lo que volvemos a cargar pro GET
        return redirect('/participants')

@app.route('/ranking')
def ranking():
    return render_template('ranking.html')

# ADICIONAL
# Creamos una ruta POST para guardar los participantes en otro fichero
@app.route('/guardar', methods=['POST'])
def guardarParticipantes():
    participantes = carregar_participants_de_fitxer()
    file = desar_participants_a_fitxer(participantes)
    if not file:
        return 'ERROR AL GUARDAR PARTICIPANTES'
    return render_template('participants.html', participantes=participantes, file=file, archivos=obtenerSaves())

# Creamos una ruta POST para eliminar los participantes actuales
@app.route('/reset', methods=['POST'])
def resetParticipantes():
    eliminarParticipantes()
    return redirect('/participants')

# Creamos una ruta POST para cargar participantes en base a un fichero dado
@app.route('/load', methods=['POST'])
def loadP():
    archivo = request.form.get('archivo')
    if not validarNombreFichero(archivo):
        return 'FICHERO NO VALIDO!'
    cargarParticipantes(archivo)
    return redirect('/participants')


### 
### PARTIDAS
###

@app.route('/partides')
def partidas():
    return render_template('partides.html')

@app.route('/partides/generarcalendario')
def generarCalendarioGET():
    return render_template('partides.html', calendario=gestio_partides.generarCalendario(carregar_participants_de_fitxer()))

@app.route('/partides/cargarcalendario')
def obtenerCalendarioGET():
    return render_template('partides.html', calendario=gestio_partides.carregar_partides_de_fitxer())

@app.route('/partides/jugarmanual')
def jugarManualGET():
    try:
        partida = int(request.args['partida'])
    except:
        return 'ERROR: LA PARTIDA SE EXPRESA DE FORMA NUMERICA'
    return render_template('partides.html', partidaJugar=partida, calendario=gestio_partides.generarCalendario(carregar_participants_de_fitxer()))

@app.route('/partides/ganador', methods=['POST'])
def ganadorPost():
    ganador = request.form.get('ganador')
    if not (ganador in carregar_participants_de_fitxer()):
        return 'GANADOR NO VALIDO!'
    if gestio_partides.guardarEntradaGanar(ganador):
        veces = puntuacions.obtenerVecesGanado(ganador)
        return render_template('partides.html', calendario=gestio_partides.carregar_partides_de_fitxer(), ganador=ganador, veces=veces)
    return ganador


###
### PUNTUACIONES Y RANKING
###

@app.route('/puntuacions')
def puntuacionesGET():
    puntuaciones = puntuacions.obtenerPuntuaciones()
    print(puntuaciones)
    return render_template('puntuacions.html', puntuaciones=puntuaciones)

# Iniciailzacion
if __name__ == '__main__':
    app.run(debug=True)