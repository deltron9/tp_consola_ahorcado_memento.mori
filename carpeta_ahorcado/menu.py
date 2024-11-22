from carpeta_ahorcado.Paquetes_Interfaz import *
from Paquetes_Validaciones import *


nombre_usuario = validar_cadena_usuario("Ingrese su nombre \nahorcado@python~$:", 'Error al ingresar su nombre. Intente nuevamente',)
mensaje_menu = f"\n\n[1] Jugar \n[2] Puntajes \n[3] Salir \n\nUsted selecciona la opción: "
simular_cargando()
while True:
    menu = validar_entero(mensaje_menu)

    match menu:
        case 1:
            elegir_idioma()
            
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