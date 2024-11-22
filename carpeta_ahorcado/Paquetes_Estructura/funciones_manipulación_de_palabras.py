import random
import json

def seleccionar_palabra() -> list:
    seleccionada = random.choice()
    return seleccionada


def elegir_idioma(msj_idioma: str) -> dict:
    '''
    Esta función recibe como parametro un ingreso que es captado con un mensaje mediante la consola
    '''
    idioma = input(msj_idioma).upper()
    
    with open("data.json", "r") as archivo:
        palabras_seleccionadas = json.load(archivo)
    if idioma == 'ES':
        return palabras_seleccionadas["ES"]
    else:
        return palabras_seleccionadas["EN"]


def p_oculta(eleccion_palabra):
    palabra_oculta = []

    for _ in eleccion_palabra:
        palabra_oculta.append('_')
    return palabra_oculta


# def palabra_elegida():
#     # Devuelve la palabra elegida según el idioma que eligio el usuario
#     eleccion = []
#     palabra_seleccionada = seleccionar_palabra()  # Obtener palabra aleatoria
#     if elegir_idioma():
#         # Agregar palabra en español
#         eleccion.append(palabra_seleccionada["ES"])
#     else:
#         eleccion.append(palabra_seleccionada["EN"])
#     return eleccion

# idioma = elegir_idioma()
# palabra_seleccionada = seleccionar_palabra()