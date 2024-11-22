from carpeta_ahorcado.Paquete_Estructura import *
from carpeta_ahorcado.Paquetes_Validaciones import *
import random
import json

# Cargamos los datos del archivo json
def cargar_palabras():
    with open("data.json", "r") as archivo:
        return json.load(archivo)


def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "a") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)


def cargar_puntaje():
    with open("score.json", "r") as archivo:
        return json.load(archivo)

with open("data.json", "r") as archivo:
    datos = json.load(archivo)

estructura_datos_usuario = {
    "nombre": "",
    "Puntaje": 0,
}

# nombre_usuario = input("\n Ingrese su nombre: ").lower()

# estructura_datos_usuario["nombre"] = nombre_usuario

# Seleccionar idioma

# Vomitamos la lógica del punto D


# def seleccionar_idioma():
#     msj_menu = 'SELECCIONE EN QUE IDIOMA EN QUE DESEA JUGAR\n\n[ES/EN]\n\n\tOPCION: '
#     menu = input(msj_menu).lower()
#     if menu == 'es':
#         return palabra_seleccionada["ES"]
#     else:
#         return palabra_seleccionada["EN"]

# Probando palabra oculta

def seleccionar_palabra(palabras) -> list:
    # Elige palabras del Json mediante random.choice
    seleccionada = random.choice(palabras)
    return seleccionada


def palabra_elegida(msj_idioma, palabras_seleccionadas):
    # Elije idioma y devuelve palabra seleccionada
    idioma = input(msj_idioma).lower()
    if idioma == 'es':
        return palabras_seleccionadas["ES"]
    else:
        palabras_seleccionadas["EN"]


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


def p_oculta(eleccion_palabra):
    palabra_oculta = []

    for _ in eleccion_palabra:
        palabra_oculta.append('_')
    return palabra_oculta


def jugar():

    msj_idioma = 'SELECCIONE UNA OPCION\n\n[es/en]\n\n\tOPCION: '
    palabras = cargar_palabras()  # Las palabras cargadas del Json
    palabras_seleccionadas = seleccionar_palabra(
        palabras)  # Las palabras del random.choice
    eleccion_palabra = palabra_elegida(msj_idioma, palabras_seleccionadas)
    palabra_oculta = p_oculta(eleccion_palabra)
    letras_usadas = []
    vidas = 6
    etapa = 1

    while vidas > 0 and '_' in palabra_oculta:
        etapa += 1
        print("\nPalabra: ", end=" ")
        for letra in palabra_oculta:
            # Imprime cada letra de la palabra oculta separada por un espacio
            print(letra, end=" ")

        print(imprimir_monigote(1))
        letra_ingresada_por_usuario = validar_cadena_en_juego(
            "Ingrese una letra: ")
        if letra_ingresada_por_usuario in letras_usadas:
            print(f"\n Esta letra ya fue utilizada!")

        letras_usadas.append(letra_ingresada_por_usuario)

        # elif letra_ingresada_por_usuario in idioma:
        # El usuario recibe un punto por cada letra adivinada
        # estructura_datos_usuario["Puntaje"] += 1
        # Se agrega la letra al diccionario de letras adivinadas
        # ADEMAS REEMPLAZA LETRA OCULTA
        # letras_correctas += 1
        if letra_ingresada_por_usuario in eleccion_palabra:
            print("\n Letra acertada !!!!!")
            puntos += 1
            # Reemplaza el _ por la letra elegida
            # for i in range(eleccion_palabra):
            #     if i == letra_ingresada_por_usuario:
            #         palabra_oculta[i] = letra_ingresada_por_usuario
            for i, l in enumerate(eleccion_palabra):
                if l == letra:
                    palabra_oculta[i] = letra_ingresada_por_usuario
        else:
            print(f"Letra incorrecta, te quedan {vidas - 1} vidas")
            vidas -= 1
            print(imprimir_monigote(etapa))

        if '_' not in palabra_oculta:
            print(f"\nGANASTEEE!! La palabra era {
                  eleccion_palabra}. Obtuviste {puntos} puntos")
        else:
            print(f"PERDISTE!! La palabra era {eleccion_palabra}")

        # gUARDAR pUNTAJE
        nombre_usuario = input("Ingrese su nombre: ")
        puntajes = cargar_puntaje()
        puntajes.append({"nombre": nombre_usuario, "puntos": puntos})

        # if letras_correctas == len(palabra_random_EN):
        #     estructura_datos_usuario["Puntaje"] += 3
        #     print(f"\n FELICIDADES !! GANASTE Y SUMASTE {
        #           estructura_datos_usuario['Puntaje']} puntos")
        break


nombre_usuario = input("\n Ingrese su nombre: ").lower()
estructura_datos_usuario["nombre"] = nombre_usuario

# Vomitamos la lógica del punto D

def jugar():

    palabra_seleccionada = random.choice(datos["ahorcado"])
    palabra_random_EN = palabra_seleccionada["EN"]
    palabra_random_ES = palabra_seleccionada["ES"]

    letras_adivinadas = [] 
    intentos = 6
    letras_correctas = 0

    
    while intentos > 0:

        letra_ingresada_por_usuario = input("\n Ingrese una letra: ")

        if letra_ingresada_por_usuario in letras_adivinadas:
            print(f"\n Esta letra ya fue utilizada!")
        elif letra_ingresada_por_usuario in palabra_random_EN:
                estructura_datos_usuario["Puntaje"] += 1 # El usuario recibe un punto por cada palabra adivinada
                letras_adivinadas.append(letra_ingresada_por_usuario) # Se agrega la letra al diccionario de letras adivinadas
                letras_correctas += 1
                print("\n Se encuentra alli !!!!!")
        else:
            """ Funcion de imprimir monigote (se le suma +1 al monigote)"""
            intentos -= 1
            print(f"\n NO ESTÁ! Te quedan {intentos} intentos")
        
        if letras_correctas == len(palabra_random_EN):
            estructura_datos_usuario["Puntaje"] += 3
            print(f"\n FELICIDADES !! GANASTE Y SUMASTE {estructura_datos_usuario['Puntaje']} puntos")
            break

    print(f"\n La palabra era: {palabra_random_EN}")



bandera_partida = True

while bandera_partida == True:
    jugar()
    continua_partida = input("\n\n Desea seguir jugando? SI/NO: ").upper()


    if continua_partida == "SI":
        print("\n En marcha! SIGAMOS")
    else:
        print("\n Adios rufián \n")
        bandera_partida = False



puntaje_guardado = guardar_puntajes(estructura_datos_usuario)

print(jugar())

def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "a") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)

puntaje_guardado = guardar_puntajes(estructura_datos_usuario)

