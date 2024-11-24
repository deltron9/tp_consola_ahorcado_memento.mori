import json

def mostrar_puntajes():
    """
Esta función abre el archivo de scores en modo lectura y aloja los datos en la variable lista
usando bubble sort ordenamos los 5 mejores punajes de manera ascendente
y por último al llamar a la función, esta usa un for iterando  devuelve un print  
    """
    with open("scores.json", "r") as file:
        lista = json.load(file)
    
    for i in range(len(lista)):                   #itera la lista
        for it in range(0, len(lista)-i-1): #itera cada elementos de la lista (desde indice 0 y muere 1 indice antes de i)
            if lista[it]['Puntaje'] < lista[it + 1]['Puntaje']:
                red = lista[it]                   #Guardamos el elemento actual
                lista[it] = lista[it + 1]         #Movemos el elemento siguiente a la posición actual
                lista[it + 1] = red               #Colocamos el elemento guardado en la siguiente posición
    
    #Mostrar solo los 5 mejores puntajes
    print("\n\tTOP 5 MEJORES PUNTAJES MUNDIALES")
    for jugador in lista[:5]:
        print(f"\n\t{jugador['nombre']}: {jugador['Puntaje']} puntos")