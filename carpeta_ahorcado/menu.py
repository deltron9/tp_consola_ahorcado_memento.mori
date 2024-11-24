import time
from Paquetes_Estructura import *
from Paquetes_Validaciones import *
from Paquetes_Interfaz import *

simular_cargando()
mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "
while True:
    menu = validar_entero(mensaje_menu)
    
    match menu:
        case 1:
            lista_palabras = elegir_idioma('Selecciona el idioma de palabras a usar \n\t[EN o ES]: ')
            if lista_palabras:
                eleccion_palabra_oculta = seleccionar_palabra(lista_palabras)
                palabra_escondida = ocultar_palabra(eleccion_palabra_oculta)
                vidas = 7
                letras_usadas = []
                etapa = 1

                while vidas > 0 and '_' in palabra_escondida:
                    print(imprimir_monigote(etapa))
                    print("\nPalabra: ", end=" ")

                    for letra in palabra_escondida:
                        print(letra, end=" ")
                    
                    print(f"\nLetras usadas: {letras_usadas}\n")
                    
                    #Verifica si se ha llegado a la etapa 7
                    if etapa == 7:
                        time.sleep(2)  #Espera 2 segundos
                        print(f"\n¡Se te acabaron las vidas! La palabra era: {eleccion_palabra_oculta}")
                        print(imprimir_monigote(8))  #Muestra el monigote final
                        break 

                    letra_ingresada_en_juego = validar_cadena_en_juego("La letra puede ser: ")
                    
                    if letra_ingresada_en_juego is None:
                        continue
                    
                    if letra_ingresada_en_juego in letras_usadas:
                        print("\n¡Esta letra ya fue adivinada!\n")
                        continue 

                    letras_usadas.append(letra_ingresada_en_juego)

                    if letra_ingresada_en_juego in eleccion_palabra_oculta:
                        palabra_escondida = ''.join(
                            letra if letra in letras_usadas else '_' 
                            for letra in eleccion_palabra_oculta
                        )
                    else:
                        etapa += 1
                        vidas -= 1 

                if '_' not in palabra_escondida:
                    print(f"\n¡Buenísimo rey! Adivinaste la palabra: {eleccion_palabra_oculta}")
        
        case 2:
            pass
        case 3:
            break  #Salir del bucle
