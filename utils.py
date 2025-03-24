# Funcions auxiliars

# Importamos el modulo que nos permite trabajar con expresiones regulares
import re

# Validacion de entrada con expresiones regulares

# Definimos una funcion que determine si un string solo contiene letras y espacios
def validName(name):
  # Expresion para verificar letras y espacios
  patron = r'^[a-zA-Z\s]+$'

  # Verificamos si cunple con el patron dado
  if re.match(patron, name):
    return True
  else:
    return False

def validarNombreFichero(nombre):
  # Expresión regular para validar el formato "dia-mes-año_hora-minuto-segundo.txt"
  PATRON_ARCHIVO = re.compile(r"^\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}\.txt$")

  if not PATRON_ARCHIVO.match(nombre):
        return False  # No cumple con el formato esperado
  else:
     return True