import turtle
import math


def draw_pythagoras_tree(t, length, level, angle=45):
    if level == 0:
        return

    for _ in range(4):
        t.forward(length)
        t.left(90)

    t.forward(length)
    t.left(angle)

    draw_pythagoras_tree(t, length * math.cos(math.radians(angle)), level - 1, angle)

    t.right(angle)
    t.backward(length)
    t.right(angle)

    draw_pythagoras_tree(t, length * math.sin(math.radians(angle)), level - 1, angle)

    t.left(angle)
    t.forward(length)
    t.left(90)


if __name__ == "__main__":
    recursion_level = int(input("Вкажіть рівень рекурсії (наприклад, 5): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("brown")

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_pythagoras_tree(t, 80, recursion_level)

    turtle.done()
