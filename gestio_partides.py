# Modul per gestionar partides
# TODO: Afegir funcions per generar partides i avançar jornades
stats = [] # Inicializamos el array donde guardaremos los ganadores ordenados de cada partida

def generar_partides(participantes):
    calendario = generarCalendario(participantes)
    print(calendario)

def desar_partides_a_fitxer(partides, fitxer):
    # TODO: Implementar lògica per desar les partides
    pass

def carregar_partides_de_fitxer(fitxer):
    # TODO: Implementar lògica per carregar les partides
    pass

def generarCalendario(participantes):
    partidas = [] # Generamos el array donde iran las tuplas de cada partida
    for i in range(len(participantes)):
        for j in range(i + 1, len(participantes)):
            # Emparejamos cada uno con otro jugador diferente, sin que se reputan
            partidas.append((participantes[i], participantes[j]))
    return partidas

# 