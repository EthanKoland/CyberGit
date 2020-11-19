import turtle
j = turtle.Turtle()

#Draw polygon
def poly(turtle,size, sides):
    for x in range(sides):
        turtle.forward(size)
        turtle.right(360/sides)
    
#Filled corner, quadratins screwed up but don't care to fix it can be done with if statemenes
def corner(turtle, quad):
    for x in range(4):
        if(x == quad):
            
            turtle.forward(50)
            
            turtle.begin_fill()
            poly(turtle, 50, 4)
            turtle.end_fill()
            turtle.forward(50)
        else:
            turtle.forward(100)
        turtle.right(360/4)

#Sqr in Sqr
def sqrINsqr(turtle, num):
    for x in range(num):
        poly(turtle,100-(x*10), 4)
        turtle.up()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.down()

sqrINsqr(j, 5)

    
    
