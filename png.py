import math
import turtle as t

def setup_screen() -> None:
    """Настройка экрана и черепахи."""
    screen = t.Screen()
    screen.setup(1000, 800)
    t.tracer(n=5, delay=0)
    t.ht()


def flower(x: float, y: float, size: float, color: str) -> None:
    """Нарисовать цветок в точке (x, y)."""
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(120)
    t.fillcolor(color)
    t.begin_fill()
    t.fd(size)
    t.rt(30)
    t.fd(2 * size)
    t.rt(150)
    t.fd(size * 0.5)
    t.lt(120)
    t.fd(size * 0.5)
    t.rt(120)
    t.fd(size * 0.5)
    t.lt(120)
    t.fd(size * 0.5)
    t.rt(150)
    t.fd(2 * size)
    t.rt(30)
    t.fd(size)
    t.dot(1)
    t.end_fill()

def triangle(a: tuple, b: tuple, c: tuple, color: str) -> None:
    """Нарисовать заполненный треугольник по трём вершинам."""
    t.pu()
    t.goto(a[0], a[1])
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for point in [a, b, c, a]:
        t.goto(point[0], point[1])
    t.end_fill()

def square(x: float, y: float, side: float, angle: float, color: str) -> None:
    """Нарисовать заполненный квадрат со стороной side, началом в (x, y)."""
    t.pu()
    t.goto(x, y)
    t.seth(angle)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.rt(90)
        t.fd(side)
    t.end_fill()

def parallelogram(x: float, y: float, a: float, b: float, angle: float,
                  color: str) -> None:
    """Нарисовать параллелограмм с началом в (x, y)."""
    t.up()
    t.goto(x, y)
    t.pd()
    t.setheading(angle)
    t.fillcolor(color)
    t.begin_fill()
    t.fd(a)
    t.left(45)
    t.fd(b)
    t.left(135)
    t.fd(a)
    t.left(45)
    t.fd(b)
    t.end_fill()

def rhomb(x: float, y: float, side: float, angle_of_rhomb: float,
          start_angle: float, color: str) -> None:
    """Нарисовать ромб."""
    t.setheading(start_angle)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.left((180 - angle_of_rhomb) / 2)
    t.forward(side)
    t.left(angle_of_rhomb)
    t.forward(side)
    t.left(180 - angle_of_rhomb)
    t.forward(side)
    t.left(angle_of_rhomb)
    t.forward(side)
    t.end_fill()

def trapezoid(x: float, y: float, low_base: float, up_base: float, side: float,
              start_angle: float, color: str) -> None:
    """Нарисовать трапецию по основаниям и боковой стороне."""
    # вычисляем угол при основании по теореме косинусов
    angle_radians = math.acos((low_base - up_base) / (2 * side))
    angle = math.degrees(angle_radians)
    t.seth(start_angle)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.fd(low_base)
    t.lt(180 - angle)
    t.fd(side)
    t.lt(angle)
    t.fd(up_base)
    t.lt(angle)
    t.fd(side)
    t.end_fill()

def rectangle(x: float, y: float, a: float, b: float, angle: float,
              color: str) -> None:
    """Нарисовать прямоугольник со сторонами a и b."""
    t.seth(angle)
    t.up()
    t.goto(x, y)
    t.pd()
    t.fillcolor(color)
    t.begin_fill()
    t.fd(a)
    t.left(90)
    t.fd(b)
    t.left(90)
    t.fd(a)
    t.left(90)
    t.fd(b)
    t.end_fill()

def jewish_star(x: float, y: float, side: float, color: str) -> None:
    """Нарисовать звезду Давида (многоугольник повторяющийся)."""
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(0)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(8):
        t.fd(side)
        t.lt(60)
        t.fd(side)
        t.rt(120)
    t.end_fill()

def snowflake_piece(x: float, y: float, a: float, b: float, angle: float,
                    color: str) -> None:
    """Одна веточка снежинки."""
    t.pu()
    t.goto(x, y)
    t.pd()
    t.setheading(angle)
    t.fillcolor(color)
    t.begin_fill()
    t.fd(a)
    t.right(30)
    t.fd(b)
    t.circle(2, 180)
    t.fd(b)
    t.right(150)
    t.fd(b)
    t.circle(2, 180)
    t.fd(b)
    t.right(150)
    t.fd(b)
    t.circle(2, 180)
    t.fd(b)
    t.right(30)
    t.fd(a)
    t.circle(5, 180)
    t.end_fill()

def ship() -> None:
    """Составной объект корабля."""
    trapezoid(20, 150, 60, 120, 40, 0, "brown")
    rectangle(48, 176.45, 4, 60, 0, "black")
    triangle((52, 236.45), (75, 226.45), (52, 216.45), "indigo")
    triangle((52, 216.45), (80, 206.45), (52, 196.45), "indigo")
    rectangle(52, 155, 30, 5, 0, "red")
    rectangle(52, 160, 30, 5, 0, "blue")
    rectangle(52, 165, 30, 5, 0, "white")

def squirrel() -> None:
    """Составной объект белки."""
    rectangle(180, 160, 30, 60, 0, "darkorange")
    triangle((185, 160), (180, 145), (190, 145), "black")
    triangle((205, 160), (200, 145), (210, 145), "black")
    rectangle(185, 170, 20, 40, 0, "wheat")
    square(215, 260, 40, 0, "gold")
    triangle((190, 180), (185, 200), (195, 200), "orange")
    triangle((200, 180), (195, 200), (205, 200), "orange")
    rectangle(189, 230, 6, 10, 0, "white")
    rectangle(195, 230, 6, 10, 0, "white")
    square(185, 250, 4, 0, "black")
    square(210, 250, 4, 0, "black")
    triangle((175, 260), (185, 260), (172, 280), "orange")
    triangle((205, 260), (215, 260), (218, 280), "orange")
    parallelogram(180, 170, 20, 30, 90, "coral")
    square(170, 276, 5, 180, "black")
    square(215, 276, 5, 180, "black")
    triangle((195, 240), (190, 245), (200, 245), "crimson")

def center_cube() -> None:
    """Центральный куб из треугольников и квадратов."""
    triangle((0, 0), (0, 100), (50, 50), "yellow")
    triangle((0, 100), (100, 100), (50, 50), "red")
    triangle((100, 100), (100, 50), (75, 75), "purple")
    triangle((100, 0), (100, 50), (50, 0), "lightblue")
    triangle((50, 50), (75, 25), (25, 25), "pink")
    square(75, 75, 35, 45, "orange")
    parallelogram(0, 0, 50, 35, 0, "green")

def cat() -> None:
    """Составной объект кота."""
    parallelogram(150, 50, 25, 20, 300, "lightblue")
    triangle((175, 25), (200, 50), (200, 0), "orange")
    triangle((205, 50), (230, 25), (205, 0), "red")
    square(200, 80, 20, 45, "lightgreen")
    triangle((185, 65), (185, 90), (200, 80), "orange")
    triangle((215, 65), (215, 90), (200, 80), "purple")

def christmas_tree() -> None:
    """Нарисовать рождественскую ёлку."""
    jewish_star(-100, 120, 10, "yellow")
    rectangle(-93, 0, 15, 30, 0, "brown")
    trapezoid(-120, 30, 70, 40, 20, 0, "green")
    trapezoid(-120, 43, 70, 40, 20, 0, "green")
    trapezoid(-120, 56, 70, 40, 20, 0, "green")
    triangle((-105, 69), (-85, 90), (-65, 69), "green")

def snowflake() -> None:
    """Полная снежинка из шести веточек."""
    for angle in range(0, 360, 60):
        snowflake_piece(-80, 190, 30, 10, angle, "white")

def peony() -> None:
    """Пион."""
    flower(-190, 65, 20, "pink")
    rectangle(-192, 0, 4, 70, 0, "green")
    parallelogram(-192, 20, 20, 30, 120, "green")
    parallelogram(-188, 30, 30, 20, 20, "green")

def swan() -> None:
    """Лебедь (составной объект)."""
    triangle((-180, 170), (-200, 190), (-160, 190), "red")
    triangle((-200, 190), (-200, 160), (-170, 160), "yellow")
    triangle((-200, 190), (-200, 160), (-215, 175), "blue")
    triangle((-215, 175), (-215, 195), (-205, 185), "pink")
    square(-205, 185, 14, 225, "green")
    parallelogram(-195, 195, 20, 14, 90, "blue")
    triangle((-205, 225), (-205, 210), (-220, 210), "orange")

def main() -> None:
    """Запуск всех фигур."""
    setup_screen()
    swan()
    peony()
    snowflake()
    christmas_tree()
    center_cube()
    cat()
    ship()
    squirrel()
    t.done()

if __name__ == "__main__":
    main()