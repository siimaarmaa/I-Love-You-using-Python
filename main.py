import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor('black')

t.penup()
t.goto(-230,175)
t.pendown()

t.pencolor('white')
t.pensize(15)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(170)
t.right(90)
t.forward(50)
t.backward(100)

t.penup()
t.goto(0,0)
t.pendown()

t.color('red')
t.begin_fill()
t.right(130)
t.forward(133)
t.circle(50,200)
t.right(140)
t.circle(50,200)
t.forward(133)
t.end_fill()

t.penup()
t.goto(140,175)
t.pendown()

t.pencolor('white')
t.right(40)
t.forward(120)
t.circle(80,180)
t.forward(120)

t.hideturtle()
turtle.done()