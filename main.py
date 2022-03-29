import turtle

screen = turtle.Screen()

bg_color = "#34ff7a"
logo_color = "#180a21"
screen.bgcolor(bg_color)


def draw_part(mod=1):
    turtle.pu()
    turtle.goto(-20 * mod, 230)
    turtle.pd()
    turtle.begin_fill()
    turtle.goto(-30 * mod, 240)
    turtle.goto(-430 * mod, 20)
    turtle.sety(-20)
    turtle.goto(-30 * mod, -240)
    turtle.goto(-20 * mod, -230)
    turtle.sety(-130)
    turtle.goto(-220 * mod, -20)
    turtle.sety(20)
    turtle.goto(-20 * mod, 130)
    turtle.sety(230)
    turtle.goto(-30 * mod, 240)
    turtle.end_fill()


turtle.color(logo_color, logo_color)
turtle.width(10)

draw_part()
draw_part(-1)

turtle.width(15)
turtle.pu()
turtle.color(bg_color, logo_color)
turtle.goto(30, 0)
turtle.pd()
turtle.begin_fill()
turtle.goto(20, 10)
turtle.goto(20, 70)
turtle.goto(180, 170)
turtle.goto(240, 130)
turtle.goto(230, 120)
turtle.goto(30, 0)
turtle.end_fill()

turtle.done()
