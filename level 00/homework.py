from turtle import *

speed(70)

width(7)
speed(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto (200, 200)
pendown()
color("red")

right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill( )

penup()
goto (80, 140)
right(60)
pendown()
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
penup()
goto(140, 140)
pendown()
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()