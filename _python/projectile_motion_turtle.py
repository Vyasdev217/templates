import math
from time import sleep
import turtle
sx=-200
sy=-200
t=turtle.Turtle()
t.speed(10)
t.hideturtle()
t.penup()
time=0
t.setposition([sx,sy])
t.pendown()
t.forward(500)
t.setposition([sx,sy])
t.left(90)
t.forward(500)
t.setposition([sx,sy])

def proj(vel, angle):
    vx=vel*math.cos(math.radians(angle))
    vy=vel*math.sin(math.radians(angle))
    sx=-200
    sy=-200
    t=turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    t.penup()
    time=0
    t.setposition([sx,sy])
    t.pendown()
    while(sy>=-200):
        sx+=vx*0.1
        sy+=(vy-9.8*time)*0.1
        t.setposition([sx,sy])
        time+=0.1
#for i in range(2,90,2):
#    proj(70,i)
proj(50,42)
sleep(5)
