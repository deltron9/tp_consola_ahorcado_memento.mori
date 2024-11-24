from Paquetes_Interfaz_De_Consola.simulacion_de_carga import simular_cargando, imprimir_bienvenida
from Paquetes_Validaciones_Ingresos.Ingresos import validar_entero
from Paquetes_Para_Iniciar_Juego import jugar, mostrar_puntajes



def menu():
    imprimir_bienvenida()
    simular_cargando()
    mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "
    while True:
        menu = validar_entero(mensaje_menu)

        match menu:
            case 1:
                jugar()
            case 2:
                mostrar_puntajes()
            case 3:
                print("Nos vemos!!!!")
                break
            case _:
                print("Opcion no válida. Intente nuevament")