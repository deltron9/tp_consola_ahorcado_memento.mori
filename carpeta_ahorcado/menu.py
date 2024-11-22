<<<<<<< HEAD
from carpeta_ahorcado.Paquetes_Interfaz import *
=======
from Paquetes_Estructura import *
>>>>>>> 0ce7493a6ff2b631e3858594af5b928b84ab185a
from Paquetes_Validaciones import *
from Paquetes_Interfaz import *

simular_cargando()
#nombre_usuario = validar_cadena_usuario("Ingrese su nombre \nahorcado@python~$:", 'Error al ingresar su nombre. Intente nuevamente',)
mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "

while True:
    menu = validar_entero(mensaje_menu)

    match menu:
        case 1:
<<<<<<< HEAD
            elegir_idioma()
            
=======
            pass
            #print(imprimir_monigote(1))
>>>>>>> 0ce7493a6ff2b631e3858594af5b928b84ab185a
        case 2:
            pass    
        case 3:
            break


def elegir_idioma():
    msj_idioma = 'SELECCIONE UNA OPCION\n\n[es/en]\n\n\tOPCION: '
    idioma = input(msj_idioma).lower()
    if idioma == 'es':
        # palabra_random_ES = palabra_seleccionada["ES"]
        return True
    else:
        # palabra_random_EN = palabra_seleccionada["EN"]
        return False