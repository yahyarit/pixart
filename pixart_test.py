import pixart
import turtle


def test_init():
    pixart.init()

    s = turtle.speed()
    assert (s == 0)

    x = turtle.xcor()
    assert (x == -200)

    y = turtle.ycor()
    assert (y == 200)

    a = turtle.isdown()
    assert (a == True)

    p = turtle.pencolor()
    assert (p == 'black')

    f = turtle.fillcolor()
    assert (f == 'white')
