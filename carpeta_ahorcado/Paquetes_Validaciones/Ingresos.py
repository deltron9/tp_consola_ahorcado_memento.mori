
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

def validar_cadena_usuario(mensaje: str, mensaje_error: str) -> str:
    '''
    Solicita una cadena y la valida por contenido.
    Retorna la cadena si es válida (solo letras y números).
    '''
    while True:
        user_input = input(mensaje).strip()  #Solicita el ingrso y elimina espacios en blanco al inicio y final
        if user_input and user_input.isalnum():  #Verifica que la cadena sea alfanumérica (solo letras y números)
            return user_input.capitalize()  #Retorna la caena válida capitalizada
        
        print(mensaje_error)  # Muestra mensaje de error si la cadena no es válida




#------------------------------Validación a la hora de jugar------------------------------------------------------
def validar_cadena_en_juego(mensaje: str, mensaje_error: str = 'Error, solo puedes ingresar 1 letra', longitud: int = 1) -> str | None: 
    '''
    Solicita una cadena y la valida por longitud y contenido.
    Retorna la cadena si es válida, o None si no lo es.
    Se valida si es alfanumérica o solo alfabética.
    '''
    caracter = str(input(mensaje))  #Solicita el ingreso
    try:
        if len(caracter) <= longitud:
            return caracter
        
    except ValueError:
        return None  # Valida la longitud
    if caracter is not None and caracter.isalpha(): #Retorna la cadena válida
        return caracter
    else:
        return mensaje_error + mensaje


