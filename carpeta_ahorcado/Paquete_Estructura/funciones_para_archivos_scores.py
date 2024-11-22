import json


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