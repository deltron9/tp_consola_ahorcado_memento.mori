import time  #Importo el módulo time para poder usar funciones relacionadas con el tiempo.
from Paquetes_Estructura import *  
from Paquetes_Validaciones import *  
from Paquetes_Interfaz import *  

simular_cargando()  #Llamamos a la función para mostrar el mensaje de carga
mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "

while True:  
    menu = validar_entero(mensaje_menu)  

    match menu:  
        case 1:
            lista_palabras = elegir_idioma('Selecciona el idioma de palabras a usar \n\t[EN o ES]: ')  #Pido al usuario que seleccione el idioma para jugar
            if lista_palabras:  #Condiciono que si se ha seleccionado una lista de palabras válida.
                eleccion_palabra_oculta = seleccionar_palabra(lista_palabras)  #llamo a la funcion que busca en el diccionario una palabra random.
                palabra_escondida = ocultar_palabra(eleccion_palabra_oculta)  #Esconde la palabra seleccionada, reemplazando letras por guiones bajos.
                vidas = 6  #Inicializa el número de vidas del jugador.
                letras_usadas = []  #Inicializo una lista para almacenar las letras que el jugador va adivinando.
                etapa = 1  # Inicializa el contador de etapas del juego. (En 1 para que inicie el con la primer pantalla)

                while vidas > 0 and '_' in palabra_escondida:  #Bucle principal del juego que funca mientras el jugador tenga vidas y haya letras por adivinar.
                    print(imprimir_monigote(etapa))  #Imprime la imagen del monigote según la etapa.
                    '''
                    considero que queda mejor así ya que arranca en la imagen inicial ya con la interfaz para juagr abajo
                    '''
                    print("\nPalabra: ", end=" ")  #Imprime el texto "Palabra: " sin saltar de línea.

                    for letra in palabra_escondida:  #Itera sobre cada letra de la palabra escondida.
                        print(letra, end=" ")  #Imprime cada letra de la palabra escondida, separadas por espacios.
                    
                    print(f"\nLetras usadas: {letras_usadas}\n")  #Muestra las letras que ya adivino el jugador.
                    
                    #Verificamos si estamos ya enla etapa 7 (cuando se han perdido todas las vidas).
                    if etapa == 7:
                        time.sleep(2)  # Espera 2 segundos para hacer la transicion de entre el ahorcado finalizado y la pantalla de game over.
                        print(f"\n¡Se te acabaron las vidas! La palabra era: {eleccion_palabra_oculta}")  #
                        print(imprimir_monigote(8))  # Muestra ela imagen del gam,e over
                        break  

                    letra_ingresada_en_juego = validar_cadena_en_juego("La letra puede ser: ")  #validacion intra juego para que solo tome 1 letra
                    if letra_ingresada_en_juego in letras_usadas:  #verificamos si la letra ingresada ya fue usada.
                        print("\n¡Esta letra ya fue adivinada!\n")    #Informa al jugador que ya adivinó esa letra.
                        continue

                    letras_usadas.append(letra_ingresada_en_juego)  #Agrega la letra ingresada a la lista de letras usadas.

                    if letra_ingresada_en_juego in eleccion_palabra_oculta:  #Verifica si la letra ingresada está en la palabra oculta.
                        palabra_escondida = ''  #Reinicia la palabra escondida como una cadena vacía.

                        for letra in eleccion_palabra_oculta:  #Itera sobre cada letra de la palabra oculta.
                            if letra in letras_usadas:  #Si la letra se adivinado:
                                palabra_escondida += letra  #Agrega la letra a la palabra escondida.
                            else:
                                palabra_escondida += '_'  #Agrega un guion bajo si la letra no ha sido adivinada.
                    else:  #Si la letra ingresada no está en la palabra oculta:
                        etapa += 1  #Aumenta una etapa lo que deriva en el printeo por pantalla de la evolucion del monigote
                        vidas -= 1

                if '_' not in palabra_escondida:  #Condicion que si la palabra se adivinó (se dilucida viendo si hay '_' en la palabra)
                    print(f"\n¡Buenísimo rey! Adivinaste la palabra: {eleccion_palabra_oculta}")

        case 2:
            pass

        case 3:
            break

