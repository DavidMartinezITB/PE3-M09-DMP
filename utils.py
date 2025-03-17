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