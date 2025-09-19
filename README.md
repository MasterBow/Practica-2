Descripción del código

Este programa utiliza la librería estándar turtle de Python para crear una ventana gráfica donde una figura (cuadrado o círculo) puede moverse con las flechas del teclado.

1. Configuración inicial

Se definen las dimensiones de la ventana (ANCHO, ALTO) y el tamaño del paso de movimiento (PASO), que indica cuántos píxeles avanza la figura por pulsación.

La variable FORMA permite elegir si la figura será un cuadrado o un círculo.

Se crea una ventana (Screen) y se ajusta el tamaño.

Se desactiva el trazo (penup()) para que la figura no deje rastro al moverse.

2. Creación de la figura

Se inicializa un objeto Turtle llamado fig.

Según el valor de FORMA, se le asigna la forma de cuadrado o círculo y se aumenta su tamaño visual.

Si la forma no es válida, se usa el estilo por defecto (classic).

3. Funciones de movimiento

Se definen cuatro funciones:

mover_izquierda() → resta al eje X.

mover_derecha() → suma al eje X.

mover_arriba() → suma al eje Y.

mover_abajo() → resta al eje Y.

Cada función actualiza la posición de la figura y refresca la pantalla.

4. Controles

Se asocian las flechas del teclado a las funciones de movimiento con onkey().

pantalla.listen() permite que la ventana detecte las pulsaciones.
🕹️ Controles

← Mover izquierda

→ Mover derecha

↑ Mover arriba

↓ Mover abajo
5. Ejecución

Se actualiza la pantalla una vez al inicio.

pantalla.mainloop() mantiene la ventana abierta hasta que el usuario la cierre manualmente.
