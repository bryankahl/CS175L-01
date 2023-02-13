import turtle

# Create the turtle object
t = turtle.Turtle()
t.speed(10)

# Draw the stop sign
t.penup()
t.goto(-50, -100)
t.pendown()
t.begin_fill()
t.color("red")
t.forward(100)
t.setheading(45)
t.forward(100)
t.setheading(90)
t.forward(100)
t.setheading(135)
t.forward(100)
t.setheading(180)
t.forward(100)
t.setheading(225)
t.forward(100)
t.setheading(270)
t.forward(100)
t.setheading(315)
t.forward(100)
t.setheading(360)
t.end_fill()

t.penup()
t.goto(-85, -10)
t.pendown()
t.color("white")
t.write("STOP", font=("Arial", 50, "bold"))

turtle.done()
