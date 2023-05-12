import random

from src.functions.handlers.jsonHandler import *
from src.functions.handlers.loggingHandler import *

# Definir diccionarios vacios para las preguntas y respuestas
preguntas = {}
respuestas = {}

# Separar los diccionarios
preguntas = QnA[0]
respuestas = QnA[1]

# Definir un diccionario vacio para poner las preguntas seleccionadas alazar
randomQuestions = {}

for i in range(3):
    # seleccionar una pregunta y su respuesta al azar
    clave = random.choice(list(preguntas.keys()))
    pregunta = preguntas.pop(clave)
    respuesta = respuestas.pop(clave)
    
    # agregar la pregunta y su respuesta como una tupla en el diccionario randomQuestions
    randomQuestions[i+1] = (pregunta, respuesta)

# escribir la pregunta y su respuesta en el archivo de registro
    logging.info(f"Pregunta {i+1}: {pregunta} - Respuesta: {respuesta}")
    
logging.info(f"Preguntas: {preguntas}")
logging.info(f"Respuestas: {respuestas}")
    
# cerrar el archivo de registro
logging.shutdown()