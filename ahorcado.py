from carpeta_ahorcado.Paquete_Estructura import *
from carpeta_ahorcado.Paquetes_Validaciones import *
import random
import json

# Cargamos los datos del archivo json


def cargar_palabras():
    with open("data.json", "r") as archivo:
        return json.load(archivo)


estructura_datos_usuario = {
    "nombre": "",
    "Puntaje": 0,
}


def guardar_estructura():
    with open("scores.json", "w") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)


def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "a") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)


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


def p_oculta(eleccion_palabra):
    palabra_oculta = []

    for _ in eleccion_palabra:
        palabra_oculta.append('_')
    return palabra_oculta


def jugar():

    palabras = cargar_palabras()  # Las palabras cargadas del Json
    palabras_seleccionadas = seleccionar_palabra(
        palabras)  # Las palabras del random.choice
    eleccion_palabra = palabra_elegida(msj_idioma, palabras_seleccionadas)
    palabra_oculta = p_oculta(eleccion_palabra)
    msj_idioma = 'SELECCIONE UNA OPCION\n\n[es/en]\n\n\tOPCION: '
    letras_usadas = []
    vidas = 6
    etapa = 1
    print(imprimir_monigote(1))

    while vidas > 0 and '_' in palabra_oculta:
        etapa += 1

        # Se le muestra la palabra oculta, las letras usadas y las vidas
        print(f"\nPalabra: {palabra_oculta}")
        print(f"Letras usadas: {letras_usadas}")
        print(F"Tienes {vidas} vidas ")

        # El se le pide una letra al usuario
        # letra_ingresada_por_usuario = validar_cadena_en_juego(
        #     "Ingrese una letra: ")
        letra_ingresada_por_usuario = ("Ingrese una letra: ")
        while letra_ingresada_por_usuario in letras_usadas:
            print(f"\n Esta letra ya fue utilizada!")
            letra_ingresada_por_usuario = validar_cadena_en_juego(
                "Ingrese una letra: ")

        letras_usadas.append(letra_ingresada_por_usuario)

        if letra_ingresada_por_usuario in eleccion_palabra:
            print("\n Letra acertada !!!!!")
            puntos += 1
            for i in range(len(eleccion_palabra)):
                if eleccion_palabra[i] == letra_ingresada_por_usuario:
                    palabra_oculta[i] = letra_ingresada_por_usuario
        else:
            print(f"Letra incorrecta, te quedan {vidas - 1} vidas")
            vidas -= 1
            print(imprimir_monigote(etapa))

        # Imprime cada letra de la palabra oculta separada por un espacio
        for letra in palabra_oculta:
            print(letra, end=" ")

    if '_' not in palabra_oculta:
        print(f"\nGANASTEEE!! La palabra era {
            eleccion_palabra}. Obtuviste {puntos} puntos")
    else:
        print(f"PERDISTE!! La palabra era {eleccion_palabra}")
        print(imprimir_monigote(8))

        # gUARDAR pUNTAJE
        nombre_usuario = input("Ingrese su nombre: ")
        estructura_datos_usuario["nombre"] = nombre_usuario
        estructura_datos_usuario["puntaje"] = puntos


def mostrar_puntajes():
    file = open("scores.json", "r+")
    text = file.read()  # todo el contedido del archivo
    print(text)
    file.close()


def menu():
    simular_cargando()
    nombre_usuario = validar_cadena_usuario(
        "Ingrese su nombre \nahorcado@python~$:", 'Error al ingresar su nombre. Intente nuevamente',)
    mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "
    while True:
        menu = validar_entero(mensaje_menu)

        match menu:
            case 1:
                jugar()
            case 2:
                mostrar_puntajes()
            case 3:
                print("Nos vemos!!!!")
                break
            case _:
                print("Opcion no válida. Intente nuevament")


print(menu())
