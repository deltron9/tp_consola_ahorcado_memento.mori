import json

def cargar_nombre_y_puntos(nombre, puntos):
    """
    esta función recibe el nombre y los puntos de el usuario
    Añade el usuario con su puntaje al archivo 'scores.json'
    """
    with open("scores.json", "r") as file:
        datos = json.load(file)

    nuevo_usuario = {"nombre": nombre, "Puntaje": puntos}
    datos.append(nuevo_usuario)

    with open("scores.json", "w") as file:
        json.dump(datos, file, indent=4)

    print(f"{nombre} acumulaste {puntos} puntos")

    

