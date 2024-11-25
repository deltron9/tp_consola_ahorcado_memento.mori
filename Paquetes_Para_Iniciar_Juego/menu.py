from Paquetes_Interfaz_De_Consola.simulacion_de_carga import *
from Paquetes_Validaciones_Ingresos.Ingresos import *
from Paquetes_Para_Iniciar_Juego import *



def menu():
    imprimir_bienvenida()
    simular_cargando()
    mensaje_menu = f"\t\t\t\t------------Ahorcado.py-----------\n\t\t\t\t----------Menu Principal----------\n\n\t\t\t\t[1] Jugar \n\t\t\t\t[2] Puntajes \n\t\t\t\t[3] Salir \n\n\t\t\t\tChoose you destiny: "
    while True:
        menu = validar_entero(mensaje_menu)

        match menu:
            case 1:
                jugar()
            case 2:
                mostrar_puntajes()
            case 3:
                print(imprimir_monigote(10))
                break
