import random
import json

def seleccionar_palabra(lista_palabras: list) -> str|bool:
    '''
    Esta función selecciona una palabra aleatoria de la lista proporcionada.
    '''
    if not lista_palabras:
        return None  #Retorna None si la lista está vacía
    seleccionada = random.choice(lista_palabras)  #Selecciona una palabra aleatoria mediante random.choice
    return seleccionada

#--------------------------------------------------------------------------------------------------------------

import json

def elegir_idioma(msj_idioma: str, mensaje_error: str = "¿Que te hablo en japonés?. \nPor favor ingresá 'EN' o 'ES'.") -> list:
    '''
    Esta función recibe como parámetro un mensaje que se muestra en la consola
    y devuelve una lista de palabras en el idioma seleccionado y validado.
    '''
    idioma = input(msj_idioma).upper()
    
    #Abrimos el archivo de data.json en modo lectura
    with open("data.json", "r") as archivo:
        palabras_seleccionadas = json.load(archivo)  # Cargamos el archivo en la variable 'palabras_seleccionadas'

    #Inicializamos una lista para las palabras seleccionadas
    palabras = []

    #Filtramos las palabras según el idioma que seleccione el usuario
    for item in palabras_seleccionadas["ahorcado"]:
        if idioma == 'ES':
            palabras.append(item["ES"])
        elif idioma == 'EN':
            palabras.append(item["EN"])
        else:
            print(mensaje_error)  #Imprimimos el mensaje de error
            return elegir_idioma(msj_idioma, mensaje_error)  #Por fin le encontré un uso a la recursividad!
            
    return palabras


#--------------------------------------------------------------------------------------------------------------

def ocultar_palabra(eleccion_palabra):
    '''
    Esta función aloja la palabra seleccionada en una lista y reemplaza cada letra por un '_'
    que luego es impreso en la consola de manera '_ _ _ _'
    '''
    palabra_oculta = []

    for _ in eleccion_palabra:
        palabra_oculta.append('_')
    return palabra_oculta
