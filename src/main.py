# Cargar ibrerias
import PySimpleGUI as sg

# Cargar src
from src.functions.handlers.fileHandler import *
from src.functions.handlers.jsonHandler import *

# Crear layout vacio
layout = []

# Imprimir info del la tabla json
for pregunta in QnA:
    preguntas_len = len(pregunta)
print(f"Cantidad de preguntas: {preguntas_len}")
for respuesta in QnA:
    respuestas_len = len(respuesta)
print(f"Cantidad de respuestas: {respuestas_len}")
print(f"Tabla cargada(Raw): {QnA}")