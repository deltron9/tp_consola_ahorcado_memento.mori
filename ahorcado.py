import random
import json

# Esta lista será iterada a medida que el usuario vaya errando en sus elecciones en las letras  
monigote = ["Inicial_sin_cabeza", "Cabeza", "Tórax", "Brazo izquierdo", "Brazo derecho", "Pierna izquierda", "Pierna derecha"]

# def imprimir_monigote(diccionario: dict, etapa: int):
#     '''
#     Esta función recibe el diccionario con las imagenes a representar en consola y la key.
#     Lo que retorna es la imagen alojada en el valor de la key que se le
#     '''
#     return diccionario[etapa]  #Retorna el valor de la clave


# Cargamos los datos del archivo json
with open("data.json", "r") as archivo:
    datos = json.load(archivo)


# Vomitamos la lógica del punto D
palabra_seleccionada = random.choice(datos["ahorcado"])
palabra_random_EN = palabra_seleccionada["EN"]
palabra_random_ES = palabra_seleccionada["ES"]

letras_adivinadas = [] 

score_letra_adivinada = 0

intentos = 0

while intentos < 6:

    letra_ingresada_por_usuario = input("Ingrese una letra: ")

    if letra_ingresada_por_usuario in palabra_random_EN:
        score_letra_adivinada = +1 # El usuario recibe un punto por cada palabra adivinada
        letras_adivinadas.append(letra_ingresada_por_usuario)
        print("Se encuentra alli !!!!!") # Se agrega la letra al diccionario de letras adivinadas
    else:
        """ Funcion de imprimir monigote (se le suma +1 al monigote)"""
        print("ERRRORRR NO ESTÁ")
        intentos += 1



