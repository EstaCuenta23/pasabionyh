# Cargar ibrerias
import PySimpleGUI as sg
import logging

# Cargar src
try:
    from src.functions.handlers.loggingHandler import *
    from src.functions.handlers.fileHandler import *
    from src.functions.handlers.jsonHandler import *
    from src.functions.handlers.randomQuestionHandler import *
except Exception as e:
    logging.error(e)

# Crear layout vacio
layout = []

# Crear dos textos
layout.append([sg.Text("Tiempo: 0.00",  key="timporizador", size=(20, 1), font=("Helvetica", 20))],)
layout.append([sg.Text("Preguntas: ", size=(20, 1), font=("Helvetica", 20))],)

# Añadir las preguntas generadas alazar
for preguntaRandom in randomQuestions:
    i =+ 1
    layout.append([sg.Text(preguntaRandom, size=(20, 1), font=("Helvetica", 20))],)
    layout.append([sg.InputText(key=f"input{i}", size=(20, 1), font=("Helvetica", 20))],)

while True

# Cerrar el archivo de registro
logging.shutdown()