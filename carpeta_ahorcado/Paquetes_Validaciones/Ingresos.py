
def validar_entero(mensaje: str, mensaje_error: str = "Error de ingreso", minimo: int = 1, maximo: int = 3) -> int|str:
    '''
    Solicita un número entero al usuario y lo valida dentro de un rango específico.
    Sigue pidiendo el número hasta que el usuario ingrese un valor válido.
    '''
    while True:
        try:
            numero = int(input(mensaje))  #Solicita el ingreso (En este caso 1, 2, o 3)
            if minimo <= numero <= maximo:  #Valida el rango (1-3)
                return numero
            else:
                print(f"{mensaje_error} (Debe estar entre {minimo} y {maximo})")
        except ValueError:
            print(f"{mensaje_error} (Debe ingresar un número entero)")


#-------------------------Validación de cadena a la hora de ingresar nombre de usuario--------------------------------------
#Esta función SOLAMENTE cumple el rol de validar el nombre del usuario

def validar_cadena_usuario(mensaje: str, mensaje_error: str) -> str:
    '''
    Solicita una cadena y la valida por contenido.
    Retorna la cadena si es válida (solo letras y números).
    '''
    while True:
        user_input = input(mensaje).strip()  #Solicita el ingrso y elimina espacios en blanco al inicio y final
        if user_input and user_input.isalnum():  #Verifica que la cadena sea alfanumérica (solo letras y números)
            return user_input.capitalize()  #Retorna la caena válida capitalizada
        
        print(mensaje_error)  #Muestra mensaje de error si la cadena no es válida




#------------------------------Validación a la hora de jugar------------------------------------------------------
#Esta funcion SOLAMENTE VALIDA EL INGRESO DE LA LETRA POR PARTE DEL USUARIO
def validar_cadena_en_juego(mensaje: str, mensaje_error: str = 'Error, solo podés ingresar 1 letra capo', longitud: int = 1) -> str | None:
    '''
    Solicita una cadena y la valida por longitud y contenido.
    Retorna la cadena si es válida, o None si no lo es.
    Se valida si es solo alfabética.
    '''
    caracter = input(mensaje)  # Solicita el ingreso

    # Verifica que el ingreso sea alfabético y tenga la longitud requerida
    if len(caracter) == longitud and caracter.isalpha():
        return caracter
    else:
        print(mensaje_error)  # Muestra el mensaje de error
        return None  # Retorna None si no es válido


#----------------------------------Validacion para idioma de palabras--------------------------------------
#Esta funcion SOLAMENTE VALIDA la seleccion de idioma
def validar_cadena_en_idioma(mensaje: str, mensaje_error: str = 'Error, selecciona [ES] o [EN]', longitud: int = 2) -> str | None:
    """
    Solicita que seleccione el idioma de palabras para jugar al usuario, valida su longitud (2 letras max) y contenido.
    Retorna la cadena si es válida, o muestra un mensaje de error si no lo es.
    La cadena tiene que ser 'ES' o 'EN'.
    """
    while True:
        cadena_idioma = input(mensaje).strip().upper()  # Solicita el ingreso y elimina espacios extra, convierte a mayúsculas
        if len(cadena_idioma) == longitud and cadena_idioma in ['ES', 'EN']:
            return True  #Retorna la cadena si es válida
        else:
            print(mensaje_error)  #Muestra mensaje de error hardcodeado
            return None  #Retorna None si no es válida