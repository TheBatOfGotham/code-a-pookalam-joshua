import turtle

#definitions

def flower(colour,radius):
   for i in range(12):
        turtle.color(colour)
        turtle.speed(0)
        turtle.begin_fill()
        turtle.circle(radius,90)
        turtle.fillcolor(colour)
        turtle.left(90)
        turtle.circle(radius,90)
        turtle.fillcolor(colour)
        turtle.left(120)
        turtle.end_fill()


def drawshape(turtle,radius,colorfill):
    turtle.begin_fill()
    turtle.pensize(4)
    turtle.color("black")
    turtle.circle(radius,extent=60)
    turtle.left(120)
    turtle.circle(radius,extent=60)
    turtle.fillcolor(colorfill)
    turtle.end_fill()
    turtle.hideturtle()


def drawflower(colour,r,num,x,y):
    petal=turtle.Turtle()
    petal.color("black")
    petal.pensize(4)
    petal.up()
    petal.goto(x,y)
    petal.down()
    petal.color(colour)
    petal.speed(0)
    no_of_petals = num   
    radius =  r
    colorfill = colour
    for i in range(no_of_petals):
        drawshape(petal,radius,colorfill)
        petal.left(360/no_of_petals) 
    petal.hideturtle()    


def flower2(colour,radius,angle):
    turtle.pensize(8)
    turtle.right(angle)
    flower(colour,radius)                

#pookalam
turtle.speed(0)
turtle.color("black")
turtle.up()
turtle.goto(0,-280)
turtle.begin_fill()
turtle.pensize(10)
turtle.down()
turtle.circle(280)
turtle.fillcolor("#391112")
turtle.end_fill()
turtle.up()
turtle.home()
turtle.down()
turtle.speed(0)
flower("#74120a",190)              #flower1
flower2("#74120a",190,15)

turtle.right(7.5)
flower("#e37418",165)              #flower2   
flower2("#e37418",165,15)

turtle.right(7.5)
flower("#eb9b3f",144)              #flower3   
flower2("#eb9b3f",144,15)

turtle.right(7.5)
flower("#dbc011",125)              #flower4   
flower2("#dbc011",125,15)

turtle.right(7.5)
flower("#c9cfc3",109)              #flower5  
flower2("#c9cfc3",109,15)

turtle.right(7.5)
flower("#1261A0",97)              #flower6 
flower2("#1261A0",97,15)

turtle.right(7.5)
flower("#1f3ca3",84)              #flower7
flower2("#1f3ca3",84,15)

turtle.right(7.5)
flower("#032543",73)              #flower8
flower2("#032543",73,15)

turtle.right(7.5)
flower("#0A1172",62)              #flower9
flower2("#0A1172",62,15)


turtle.color("black")
drawflower("#FAFA33",50,15,0,60)
drawflower("#ECFFDC",50,15,45,45)
drawflower("#FFFAA0",50,15,60,0)
drawflower("#93C572",50,15,45,-45)
drawflower("#FFE5B4",50,15,0,-60)
drawflower("#ECFFDC",50,15,-45,-45)
drawflower("#FFFFF0",50,15,-60,0)
drawflower("#F89880",50,15,-45,45)
drawflower("#FFB6C1",60,15,0,0)
#drawflower("#FFFFF0",60,15,-30,30)
#drawflower("#F8C8DC",60,1,0,-60)

turtle.hideturtle()

turtle.done()        








