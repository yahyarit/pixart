import pixart
import turtle


def test_init():
    pixart.init()
    
    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor()
    assert(x==-300)

    y=turtle.ycor()
    assert(y==300)

    a=turtle.isdown()
    assert(a==false)

    p=turtle.pencolor()
    assert(p=='black')

    f=turtle.fillcolor()
    assert(f=='white')


    