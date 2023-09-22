from turtle import *
import colorsys


speed(100)
bgcolor("black")
h = 0
# Dibujar el tallo verde del girasol
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# /////// 
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("red") 
        h += 0.005
        rt(90)
        circle(190 - j * 10, 90)
        lt(90)
        circle(190 - j * 10, 90)
        rt(180)
    circle(40, 24)
penup()
goto(-20, 0)
pendown()
color("black")
begin_fill()
circle(44) 
end_fill()
done()