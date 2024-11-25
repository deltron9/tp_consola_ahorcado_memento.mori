▶ ☠ ✞ Trabajo Práctico: Desarrollo del juego del ahorcado 웃 en consola ✞ ☠ ◀</br>
</br>
Grupo: ▌║█║▌│║▌│║▌║▌█║ 𝗠𝗲𝗺𝗲𝗻𝘁𝗼 𝗠𝗼𝗿𝗶 ▌│║▌║▌│║║▌█║▌║█ </br>
</br>
 Integrantes: </br>
 𝓒𝓻𝓲𝓼𝓽𝓲𝓪𝓷 𝓒𝓸𝓵𝓵𝓪𝓷𝓽𝓮 (Planificación inicial, desarrollo de funciones, modularización, diseños de monigote y pantallas de carga, documentación detallada y testeo)</br>
 𝓐𝓷𝓭𝓻𝓮𝓼 𝓑𝓮𝓷𝓮𝓰𝓪𝓼 (Planificación inicial, desarrollo de funciones, y documentación detallada)</br>
 𝓜𝓪𝓻𝓬𝓸𝓼 𝓐𝓵𝓶𝓲𝓻𝓸𝓷 (Desarrollo de lógica principal, desarrollo de funciones y documentación detallada)</br>
</br>
Agradecimientos a: 𝙑𝙖𝙡𝙚𝙣𝙩𝙞𝙣 𝘿'𝙖𝙙𝙖𝙢𝙤 y 𝙋𝙖𝙗𝙡𝙤 𝘾𝙤𝙣𝙙𝙚 (∩ ͡° ͜ʖ ͡°)⊃
</br>
Enunciado</br>
Objetivo:</br>
Desarrollar el clásico juego del Ahorcado en una versión de consola en Python. Los
estudiantes deberán implementar todas las funcionalidades necesarias para que el juego
sea jugable en modo texto.</br>
</br>
Detalles del Ejercicio</br>
</br>
El juego del Ahorcado consiste en adivinar una palabra letra por letra antes de que el
monigote del ahorcado se complete. Los datos de las palabras estarán almacenados en un
archivo JSON.</br>
</br>
Datos iniciales en archivo JSON (data.json):</br>
● ID </br>
● Palabra en español </br>
● Palabra en inglés </br>
</br>
Requerimientos</br> 
A. Cargar el archivo data.json.</br>
</br>
● Cargar un archivo JSON con palabras en español e inglés.</br>
● Permitir que el juego seleccione aleatoriamente una palabra para adivinar.</br>
</br>
B. Selección de idioma.</br>
● Agregar la opción para seleccionar el idioma de las palabras en español o en inglés</br>
al inicio del juego.</br>
</br>
C. Representación del Monigote en Consola.</br>
● Representar el monigote en la consola con texto. La figura debe mostrarse
progresivamente a medida que el jugador falla intentos. El monigote se debe
construir de la siguiente manera:</br>
○ Cabeza</br>
○ Tórax</br>
○ Brazo izquierdo</br>
○ Brazo derecho</br>
○ Pierna izquierda</br>
○ Pierna derecha</br>
</br>
D. Lógica del Juego.</br>
● El jugador tendrá seis (6) intentos para adivinar la palabra.</br>
● Por cada intento fallido, se añadirá una parte al monigote.</br>
● Si el jugador adivina una letra correctamente, se descubrirá esa letra en la palabra</br>
oculta.</br>
● Mostrar las letras usadas y la palabra con las letras descubiertas después de cada</br>
intento.</br>
</br>
E. Sistema de Puntaje.</br>
● Por cada letra correcta adivinada, el jugador recibirá un punto.</br>
● Al descubrir la palabra, el jugador suma puntos en base a la cantidad de letras de la
palabra.</br>
</br>
F. Guardado de Puntaje en Archivo JSON.</br>
● Al finalizar el juego, pedir el nombre del jugador y almacenar el puntaje en un archivo
scores.json.</br>
● Mostrar los cinco (5) mejores puntajes al final de cada partida.</br>
</br>
G. Interfaz del Menú en Consola.</br>
● Incluir un menú inicial en consola con las siguientes opciones:</br>
1. Jugar</br>
2. Puntajes</br>
3. Salir</br>
</br>
H. Mostrar los Mejores Puntajes</br>
● La opción "Puntajes" del menú debe mostrar los cinco mejores puntajes junto con el
nombre del jugador, en orden descendente.</br>
</br>
Opcional</br>
1. Efectos Visuales:</br>
○ Añadir una animación de texto o símbolos para hacer el juego más visual y
entretenido.</br>
</br>
2. Mensajes Personalizados:</br>
○ Agregar mensajes personalizados cada vez que se adivine una letra o
cuando el jugador pierda.</br>
</br>
Ejemplo de Ejecución</br>
--- Menú Principal ---</br>
1. Jugar</br>
2. Puntajes</br>
3. Salir</br>
Seleccione una opción: 1</br>
Seleccione el idioma (es/en): es</br>
Palabra: _ _ _ _ _ _ _</br>
Letras usadas:</br>
Intentos restantes: 6</br>
Introduce una letra: e</br>
¡Bien hecho! Adivinaste una letra.</br>
Palabra: e _ e _ a _ e</br>
Letras usadas: e</br>
Intentos restantes: 6</br>
Introduce una letra: n</br>
Letra incorrecta. Te quedan 5 intentos.</br>
...</br>
¡Ganaste! La palabra era 'elefante'. Obtuviste 8 puntos.</br>
Introduce tu nombre: Juan</br>
¡Puntaje guardado!</br>
--- Mejores Puntajes ---</br>
1. Juan - 8 puntos</br>
2. Ana - 7 puntos</br>
...</br>
</br>
Entrega:</br>
</br>
● Código Python (ahorcado.py)</br>
● Archivo JSON con palabras (data.json)</br>
● Archivo JSON con puntajes (scores.json)</br>
</br>
Evaluación:</br>
● Cumplimiento de cada uno de los requerimientos.</br>
● Corrección en la lógica del juego y gestión de errores.</br>
● Creatividad en la representación del monigote y la interfaz de
texto.</br>
