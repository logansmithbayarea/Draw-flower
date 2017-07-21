import turtle

def draw_square(s_turtle):
    for s in range(1,5):
        s_turtle.forward(110)
        s_turtle.right(90)

def draw_circle(f_turtle):
    for f in range(1,5):
        f_turtle.circle(80)

def draw_triangle(t_turtle):
    for t in range(1,3):
        t_turtle.left(60)
        t_turtle.forward(90)
        

def draw_shapes():
    window  = turtle.Screen()
    window.bgcolor("black")
    
    Kevin = turtle.Turtle()
    Kevin.shape("square")
    Kevin.color("white")
    Kevin.speed(100)
    for L in range(1,37):
        draw_square(Kevin)
        Kevin.right(10)
        
    Alice = turtle.Turtle()
    Alice.shape("circle")
    Alice.color("red")
    Alice.speed(100)
    for H in range(1,37):
        draw_circle(Alice)
        Alice.right(10)

    Stef = turtle.Turtle()
    Stef.shape("arrow")
    Stef.color("blue")
    Stef.speed(60)
    for T in range(1,37):
        Stef.penup()
        Stef.setpos(0,0)
        Stef.pendown()
        draw_triangle(Stef)
        Stef.right(10)
    Stef.penup()
    Stef.setpos(0,0)
    Stef.pendown()
    Stef.right(90)
    Stef.setpos(0,-165)
    Stef.color("green")
    Stef.pensize(10)
    Stef.forward(250)

    window.exitonclick()


draw_shapes()
