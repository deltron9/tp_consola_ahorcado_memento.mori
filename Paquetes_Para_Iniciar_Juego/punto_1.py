import time  #Importo el módulo time para poder usar funciones relacionadas con el tiempo. (lo uso en la linea 31 para la transicion de printeos)
from Paquetes_Relacionados_Json import elegir_idioma, seleccionar_palabra, ocultar_palabra, cargar_nombre_y_puntos 
from Paquetes_Validaciones_Ingresos import *  
from Paquetes_Interfaz_De_Consola import *  
from Paquetes_Para_Iniciar_Juego.punto_2 import *

def jugar():
    lista_palabras = elegir_idioma('Selecciona el idioma de palabras a usar \n\t[EN o ES]: ')  #Pido al usuario que seleccione el idioma para jugar
    if lista_palabras:  #Condiciono que si se ha seleccionado una lista de palabras válida.
        eleccion_palabra_oculta = seleccionar_palabra(lista_palabras)  #llamo a la funcion que busca en el diccionario una palabra random.
        palabra_escondida = ocultar_palabra(eleccion_palabra_oculta)  #Esconde la palabra seleccionada, reemplazando letras por guiones bajos.
        vidas = 7 #la vida la hardcodeo en 7
        letras_usadas = []  #Inicializo una lista para almacenar las letras que el jugador va adivinando.
        puntos_usuario = 0 
        etapa = 1  # Inicializa el contador de etapas del juego. (En 1 para que inicie el con la primer pantalla)

        while vidas > 0 and '_' in palabra_escondida and etapa <= 7:  # Bucle principal del juego que funca mientras el jugador tenga vidas y haya letras por adivinar.
            print(imprimir_monigote(etapa))  #Imprime la imagen del monigote según la etapa.

            print("\nPalabra: ", end=" ")  #Imprime el texto "Palabra: " sin saltar de línea.

            for letra in palabra_escondida:  #Itera sobre cada letra de la palabra escondida.
                print(letra, end=" ")  #Imprime cada letra de la palabra escondida, separadas por espacios.
            
            print(f"\nLetras usadas: {letras_usadas}\n")  #Muestra las letras que ya adivino el jugador.
            print(f'Vidas: {vidas - 1}')
            

            letra_ingresada_en_juego = validar_cadena_en_juego("La letra puede ser: ")
            
            if letra_ingresada_en_juego in letras_usadas:  #verificamos si la letra ingresada ya fue usada.
                print("\n¡Esta letra ya fue adivinada!\n")  #Informa al jugador que ya adivinó esa letra.
                continue

            letras_usadas.append(letra_ingresada_en_juego)  #Agrega la letra ingresada a la lista de letras usadas.

            # Verifica si la letra ingresada está en la palabra oculta.
            if letra_ingresada_en_juego in eleccion_palabra_oculta:
                print("\n¡Letra acertada!!!!!")
                puntos_usuario += eleccion_palabra_oculta.count(letra_ingresada_en_juego)  #Suma puntos por cada aparición de la letra
                for i in range(len(eleccion_palabra_oculta)):
                    if eleccion_palabra_oculta[i] == letra_ingresada_en_juego:
                        palabra_escondida[i] = letra_ingresada_en_juego  #Actualiza la palabra escondida con la letra acertada

            else:  #Si la letra ingresada no está en la palabra oculta:
                etapa += 1  #Aumenta una etapa lo que deriva en el printeo por pantalla de la evolución del monigote.
                vidas -= 1  # Pierde una vida
        
            if etapa == 7:
                #Espera 2 segundos para hacer la transición entre el ahorcado finalizado y la pantalla de game over
                time.sleep(2)
                print(f"\n---------------------------------------------------------------------------------------\n¡Se te acabaron las vidas! \nLa palabra era: {eleccion_palabra_oculta}")
                print(imprimir_monigote(8))  #
                break  #termina el juego acá
            elif '_' not in palabra_escondida:  #Condición que si la palabra se adivinó (se dilucida viendo si hay '_' en la palabra)
                time.sleep(2)
                print(f"\n{imprimir_monigote(9)} \n¡Buenísimo rey! Adivinaste la palabra: [{eleccion_palabra_oculta}] \n\tobtuviste {puntos_usuario} puntos.\n")
                break  #Termina el juego si la palabra fue adivinada

        # Guardar puntaje
        nombre_usuario = validar_cadena_usuario('Ingrese su nombre: ', 'ERROR')
        cargar_nombre_y_puntos(nombre_usuario, puntos_usuario)
        mostrar_puntajes()
        time.sleep(2)
        