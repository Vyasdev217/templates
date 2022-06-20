vel=52
a=45

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
    #t.speed(10)
    t.speed(round(10*pow((vx**2)+(vy**2),0.5)/vel))
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
R=(vel**2)*math.sin(math.radians(2*a))/9.8
t.penup()
t.setposition((-325,200))
t.pendown()
t.write("Initial veocity:"+str(vel)+"\n"+"Initial inclination:"+str(a)+" degree\n"+"Max. height:"+str(round(R*math.sin(math.radians(2*a)),2))+"\n"+"Range:"+str(round(R,2))+"\n")
proj(vel,a)
sleep(5)
