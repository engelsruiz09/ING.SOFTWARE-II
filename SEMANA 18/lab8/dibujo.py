import turtle
import random
import sys
import ctypes

def check_modules():
    modules = ['turtle', 'random']
    missing_modules = []

    for module in modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        ctypes.windll.user32.MessageBoxW(0, "Faltan los siguientes módulos que son necesarios para ejecutar la aplicación: " + ", ".join(missing_modules) + "\nPor favor, instale los módulos faltantes antes de ejecutar la aplicación.", "Error de módulos faltantes", 1)
        return False
    return True
 
def draw_random_shapes():
    shapes = random.randint(1, 5)  # Numero aleatorio de formas a dibujar en un grupo
    for _ in range(shapes):
        sides = random.randint(2, 10)
        length = random.randint(10, 100)
        angle = 360 / sides
        turtle.begin_fill()
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(angle)
        turtle.end_fill()
        turtle.right(random.randint(0, 360))  # Gira un ángulo aleatorio antes de la siguiente forma

def main():
    if check_modules():  # Verifica los módulos antes de ejecutar el resto del programa
        turtle.speed(0)
        turtle.bgcolor("white")

        while True:
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color(color, color)  # Establece tanto el color del lápiz como el de relleno
            draw_random_shapes()

if __name__ == "__main__":
    main()

