# Modul per gestionar puntuacions
import gestio_participants
import csv
from collections import Counter

FICHERO_ESTADISTICAS = 'estadisticas.txt'

# TODO: Afegir funcions per actualitzar puntuacions i generar rànquings

def obtenerPuntuaciones(fichero=FICHERO_ESTADISTICAS):
    jugadores = gestio_participants.carregar_participants_de_fitxer()
    with open(fichero, 'r') as f:
        ganados = [l[:-1] for l in f.readlines()]
    conteoGanadores = Counter(ganados)
    victoriasFinal = {jugador: conteoGanadores[jugador] for jugador in jugadores}
    
    return victoriasFinal
    

def obtenerVecesGanado(ganador, fichero=FICHERO_ESTADISTICAS):
  with open(fichero, 'r') as f:
      return [l[:-1] for l in f.readlines()].count(ganador)