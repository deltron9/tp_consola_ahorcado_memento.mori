import json

def mostrar_puntajes():
    file = open("scores.json", "r+")
    text = file.read()  # todo el contedido del archivo
    print(text)
    file.close()