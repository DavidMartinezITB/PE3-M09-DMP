# Importamos el modulo que nos permite trabajar con fechas
import datetime

# Modul per gestionar participants
SAVES_DIR = 'saves'
FICHERO_PARTICIPANTES = 'participantes.txt'

# TODO: Afegir funcions per afegir, validar i desar participants

def afegir_participant(nom):
    try:
        with open(FICHERO_PARTICIPANTES, 'a') as f:
            f.write(nom + '\n')
        return True
    except:
        return False

def desar_participants_a_fitxer(participants):
    if not participants:
        return False
    nombreFichero = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".txt"
    filePath = SAVES_DIR + '/' + nombreFichero
    try:
        with open(filePath, 'w') as f:
            f.write("\n".join(participants))
        return nombreFichero
    except:
        return False

# Funcion que devuelve los participantes actuales
def carregar_participants_de_fitxer(fitxer=FICHERO_PARTICIPANTES):
    try:
        with open(fitxer, 'r') as f:
            participantes = []
            for line in f.readlines():
                participantes.append(line.strip())
    except:
        return []
    return participantes

# ADICIONAL
# Eliminar participantes
def eliminarParticipantes():
    open(FICHERO_PARTICIPANTES, "w").close()