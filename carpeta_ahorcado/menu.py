from Paquetes_Estructura import *
from Paquetes_Validaciones import *
from Paquetes_Interfaz import *

simular_cargando()
#nombre_usuario = validar_cadena_usuario("Ingrese su nombre \nahorcado@python~$:", 'Error al ingresar su nombre. Intente nuevamente',)
mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "

while True:
    menu = validar_entero(mensaje_menu)

    match menu:
        case 1:
            pass
            #print(imprimir_monigote(1))
        case 2:
            pass    
        case 3:
            break