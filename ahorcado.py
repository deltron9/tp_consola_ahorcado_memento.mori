import random
import json

# def imprimir_monigote(diccionario: dict, etapa: int):
#     '''
#     Esta función recibe el diccionario con las imagenes a representar en consola y la key.
#     Lo que retorna es la imagen alojada en el valor de la key que se le
#     '''
#     return diccionario[etapa]  #Retorna el valor de la clave


# Cargamos los datos del archivo json
with open("data.json", "r") as archivo:
    datos = json.load(archivo)

nombre_usuario = input("Ingrese su nombre: ")

estructura_datos_usuario = {
    "nombre": {nombre_usuario},
    "Puntaje": 0,
}

# Vomitamos la lógica del punto D
palabra_seleccionada = random.choice(datos["ahorcado"])
palabra_random_EN = palabra_seleccionada["EN"]
palabra_random_ES = palabra_seleccionada["ES"]

letras_adivinadas = [] 

intentos = 0

while intentos < 6:

    letra_ingresada_por_usuario = input("Ingrese una letra: ")
    
    if letra_ingresada_por_usuario in palabra_random_EN:
        estructura_datos_usuario["Puntaje"] += 1 # El usuario recibe un punto por cada palabra adivinada
        letras_adivinadas.append(letra_ingresada_por_usuario)
        print("Se encuentra alli !!!!!") # Se agrega la letra al diccionario de letras adivinadas
        if letra_ingresada_por_usuario in letras_adivinadas:
            print("Esta letra ya fue utilizada!")
    else:
        """ Funcion de imprimir monigote (se le suma +1 al monigote)"""
        print(f"NO ESTÁ! Te quedan {intentos} intentos")
        intentos += 1


def guardar_puntajes(estructura_datos_usuario):
    with open("scores.json", "w") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)


