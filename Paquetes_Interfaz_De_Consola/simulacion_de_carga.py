import time

def imprimir_bienvenida():
    print('''

    ███╗░░░███╗███████╗███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░  ███╗░░░███╗░█████╗░██████╗░██╗
    ████╗░████║██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██║
    ██╔████╔██║█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║  ██╔████╔██║██║░░██║██████╔╝██║
    ██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║  ██║╚██╔╝██║██║░░██║██╔══██╗██║
    ██║░╚═╝░██║███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝  ██║░╚═╝░██║╚█████╔╝██║░░██║██║
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝

    ██████╗░██████╗░███████╗░██████╗███████╗███╗░░██╗████████╗░█████╗░░░░░░░░░░
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝████╗░██║╚══██╔══╝██╔══██╗░░░░░░░░░
    ██████╔╝██████╔╝█████╗░░╚█████╗░█████╗░░██╔██╗██║░░░██║░░░███████║░░░░░░░░░
    ██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██║░░░░░░░░░
    ██║░░░░░██║░░██║███████╗██████╔╝███████╗██║░╚███║░░░██║░░░██║░░██║██╗██╗██╗
    ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝╚═╝''')
    time.sleep(3)
    print('''

    ░█████╗░██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██████╗░░█████╗░░░░██████╗░██╗░░░██╗
    ██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗░░░██╔══██╗╚██╗░██╔╝
    ███████║███████║██║░░██║██████╔╝██║░░╚═╝███████║██║░░██║██║░░██║░░░██████╔╝░╚████╔╝░
    ██╔══██║██╔══██║██║░░██║██╔══██╗██║░░██╗██╔══██║██║░░██║██║░░██║░░░██╔═══╝░░░╚██╔╝░░
    ██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝██║░░██║██████╔╝╚█████╔╝██╗██║░░░░░░░░██║░░░
    ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░''')
    return 'Abriendo programa...'
    


def simular_cargando(mensaje: str = 'Cargando') -> str:
#Esta función simula un carga de juego y muestra el mensaje en pantalla de la variable BIENVENIDA
    mensaje_impresion = mensaje
    suma_puntos = 0
    print(f"\t\t\t\t{mensaje_impresion}")
    for i in range(3):
        mensaje_impresion += '.'
        print(f"\t\t\t\t{mensaje_impresion}")
        time.sleep(1)  #Pausa de un segundo entre cada impresión
        suma_puntos += 1
        if suma_puntos == 3:
            print(f'\t\t\t\t¡Carga completa!\n')
            time.sleep(2)