import csv

# Modul per gestionar partides
# TODO: Afegir funcions per generar partides i avançar jornades
stats = [] # Inicializamos el array donde guardaremos los ganadores ordenados de cada partida
FICHERO_PARTIDAS = 'partidas.txt'
FICHERO_ESTADISTICAS = 'estadisticas.txt'
def generarCalendario(participantes):
    partidas = [] # Generamos el array donde iran las tuplas de cada partida
    for i in range(len(participantes)):
        for j in range(i + 1, len(participantes)):
            # Emparejamos cada uno con otro jugador diferente, sin que se reputan
            partidas.append((participantes[i], participantes[j]))
    desar_partides_a_fitxer(partidas)
    return partidas

def desar_partides_a_fitxer(partides, fitxer=FICHERO_PARTIDAS):
    # Vaciamos fichero
    with open(fitxer, 'w') as f:
        f.write('')
    # Agregamos partidas al fichero
    with open(fitxer, 'a') as f:
        for partida in partides:
            f.write(f'{partida[0]};{partida[1]}\n')

def carregar_partides_de_fitxer(fitxer=FICHERO_PARTIDAS):
    partidas = []
    with open(fitxer, 'r') as f:
        data = [l[:-1] for l in f.readlines()]
    
    for partida in data:
        players = partida.split(';')
        partidas.append((players[0], players[1]))
    return partidas

def guardarEntradaGanar(ganador):
    with open(FICHERO_ESTADISTICAS, 'a') as f:
        f.write(f'{ganador}\n')
        return True