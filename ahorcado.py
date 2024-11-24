from carpeta_ahorcado.Paquetes_Estructura import *
from carpeta_ahorcado.Paquetes_Validaciones import *
import random
import json

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

