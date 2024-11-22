from carpeta_ahorcado.Paquetes_Estructura import *
from carpeta_ahorcado.Paquetes_Validaciones import *
import random
import json

def jugar():

    msj_idioma = 'SELECCIONE UNA OPCION\n\n[es/en]\n\n\tOPCION: '
    palabras = cargar_palabras()  # Las palabras cargadas del Json
    palabras_seleccionadas = seleccionar_palabra(palabras)  #Las palabras del random.choice
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
            print(f"\nGANASTEEE!! La palabra era {eleccion_palabra}. Obtuviste {puntos} puntos")
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
def elegir_idioma():
    ingreso_usuario = input("Elija un idioma EN/ES: ").upper()
    if ingreso_usuario == "EN":
        palabra_random_EN = palabra_seleccionada["EN"]
    else:
        palabra_random_ES = palabra_seleccionada["ES"]

    return 

def jugar():

    # palabra_seleccionada = random.choice(datos["ahorcado"])
    # palabra_random_EN = palabra_seleccionada["EN"]
    # palabra_random_ES = palabra_seleccionada["ES"]

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



<<<<<<< HEAD
# # Cargamos los datos del archivo json
# with open("data.json", "r") as archivo:
#     datos = json.load(archivo)


###################################### 


# estructura_datos_usuario = {
#     "nombre": "",
#     "Puntaje": 0,
# }

# Recibe como parámetro la estructura de ejemplo tal cual está comentada arriba
def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "r") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)
    print("Puntaje guardado!")



# Ordena la lista en modo burbuja, en órden DESCENDENTE
def ordenar_lista(lista): 
    
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j]["Puntaje"] < lista[j + 1]["Puntaje"]: # Se accede al valor de la key "Puntaje"
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista
    

# Retorna los puntajes ordenados al haber recibido la funcion burbuja
def ordenar_puntajes(ordenar_lista):
    with open("scores.json", "r") as archivo:
        puntajes_mas_altos_cargados = json.load(archivo)

    puntajes_ordenados = ordenar_lista(puntajes_mas_altos_cargados)
    
    return puntajes_ordenados



def mostrar_puntajes_mas_altos(puntajes_ordenados:list):
    
    contador = 1
    print("--- Mejores Puntajes ---")
    for nombre in puntajes_ordenados:
        # Se accede al diccionario para poder printear por cada iteración
        print(f'{contador} . {nombre["nombre"]} - {nombre["Puntaje"]}') 
        contador += 1
        if contador > 5: # Condición de corte para poder mostrar SOLAMENTE los primeros 5 máximos puntajes
            break


# ----  Ejemplo de uso ----

#puntajes_ya_ordenados = ordenar_puntajes()
#mostrar_puntajes_mas_altos(puntajes_ya_ordenados)
=======
puntaje_guardado = guardar_puntajes(estructura_datos_usuario)

print(jugar())

def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "a") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)

puntaje_guardado = guardar_puntajes(estructura_datos_usuario)

>>>>>>> 0ce7493a6ff2b631e3858594af5b928b84ab185a
