import json

estructura_datos_usuario = {
    "nombre": "",
    "Puntaje": 0,
}


def guardar_estructura():
    with open("scores.json", "w") as scores:
        json.dump(estructura_datos_usuario, scores, indent=4)


def cargar_puntaje():
    '''
    Esta función abre el archivo scores.json en modo lectura.
    Carga el archivo mediante jsoin.load en la variable 'puntaje_cargado'.
    y retorna la variable 
    '''
    with open("ahorcado\scores.json", "r") as archivo:
        puntaje_cargado = json.load(archivo)
        return puntaje_cargado


def guardar_puntajes(estructura_datos_usuario):
    '''
    Esta función abre el archivo 'scores.json' en modo append. 
    lo cual cualquier dato que se escriba se agregará al final del archivo, sin borrar lo que ya exista. 
    Se utiliza la función json.dump() para escribir (o guardar) la variable 'estructura_datos_usuario' en el archivo, 
    formateándola con una sangría de 4 espacios (usando indent= 4) para que sea más legible.
    '''
    with open("scores.json", "a") as scores: 
        json.dump(estructura_datos_usuario, scores, indent=4)