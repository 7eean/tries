import turtle as t

def dibujar_escudo():
    t.bgcolor("#ffffff")  # Color de fondo blanco
    t.speed(1)  # Velocidad de dibujo

    # Dibuja el círculo azul
    t.color("#0055a4")  # Azul de Boca Juniors
    t.begin_fill()
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.circle(150)
    t.end_fill()

    # Dibuja la franja amarilla
    t.color("#ffd100")  # Amarillo de Boca Juniors
    t.begin_fill()
    t.penup()
    t.goto(-150, 0)
    t.setheading(0)
    t.pendown()
    t.forward(300)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(60)
    t.end_fill()

    t.hideturtle()
    t.done()

if __name__ == "__main__":
    dibujar_escudo()
