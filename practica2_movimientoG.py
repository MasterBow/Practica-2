import turtle

# ------- Configuración -------
ANCHO, ALTO = 800, 600
PASO = 20            # pixels que se mueve por pulsación
FORMA = 'cuadrado'   # 'cuadrado' o 'circulo'

# Ventana
pantalla = turtle.Screen()
pantalla.title("Mover figura con flechas (sin rastro)")
pantalla.setup(width=ANCHO, height=ALTO)
pantalla.tracer(100)  # mejora el refresco (se actualiza manualmente)

# "Jugador" (la figura)
fig = turtle.Turtle()
fig.penup()                  # evita dejar rastro
fig.speed('fastest')         # movimientos instantáneos
fig.setheading(0)            # evitar rotación visual indeseada

# elegir forma visual
if FORMA.lower() == 'cuadrado':
    fig.shape('square')
    # opcional: aumentar tamaño visual del "cuadrado"
    fig.shapesize(stretch_wid=2, stretch_len=2)
elif FORMA.lower() == 'circulo':
    fig.shape('circle')
    fig.shapesize(stretch_wid=2, stretch_len=2)
else:
    # fallback
    fig.shape('classic')

# ------- Funciones de movimiento -------
def mover_izquierda():
    x = fig.xcor() - PASO
    fig.setx(x)
    pantalla.update()

def mover_derecha():
    x = fig.xcor() + PASO
    fig.setx(x)
    pantalla.update()

def mover_arriba():
    y = fig.ycor() + PASO
    fig.sety(y)
    pantalla.update()

def mover_abajo():
    y = fig.ycor() - PASO
    fig.sety(y)
    pantalla.update()

# ------- Asociar teclas -------
pantalla.listen()
pantalla.onkey(mover_izquierda, "Left")
pantalla.onkey(mover_derecha,   "Right")
pantalla.onkey(mover_arriba,    "Up")
pantalla.onkey(mover_abajo,     "Down")

# mostrar inicialmente
pantalla.update()

# Mantener ventana abierta
pantalla.mainloop()
