import turtle

xmax=-200
xmin= -xmax
ymax=200
ymin=-ymax



def init():
    turtle.reset()
    turtle.goto(xmax,ymax)
    turtle.speed(0)
    turtle.down()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    