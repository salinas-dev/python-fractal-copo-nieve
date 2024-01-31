import turtle

# Función para dibujar una curva de Koch de un nivel dado
def koch_snowflake(turtle, length, level):
    if level == 0:
        turtle.forward(length)
        turtle.color("red")  # Cambia el color de la línea
        return
    length /= 3.0
    koch_snowflake(turtle, length, level - 1)
    turtle.left(60)
    koch_snowflake(turtle, length, level - 1)
    turtle.right(120)
    koch_snowflake(turtle, length, level - 1)
    turtle.left(60)
    koch_snowflake(turtle, length, level - 1)

# Inicializa la ventana de Turtle
window = turtle.Screen()
window.bgcolor("white")

# Crea una tortuga para dibujar el copo de nieve
flake = turtle.Turtle()
flake.speed(0)  # Ajusta la velocidad de dibujo

# Mueve la tortuga a la posición inicial
flake.penup()
flake.goto(-200, 100)
flake.pendown()

# Dibuja el copo de nieve de Koch
for _ in range(3):
    koch_snowflake(flake, 400, 4)
    flake.right(120)

# Cierra la ventana haciendo clic en ella
window.exitonclick()