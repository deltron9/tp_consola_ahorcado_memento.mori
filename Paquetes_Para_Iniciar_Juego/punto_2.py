import json

def mostrar_puntajes():
    with open("ahorcado/scores.json", "r") as file:
        datos = json.load(file)

    for usuario in datos:     # Recorrer la lista y mostrar los nombres y puntajes de los usuarios
        print(f"Nombre: {usuario['nombre']} - Puntaje: {usuario['Puntaje']}")
    '''
    Loque hace el For es imprimir los datos de scores sin el formato de diccionario
    si lo poniamos solamente con el return de datos, imprime por pantalla el json en crudo.
    '''



