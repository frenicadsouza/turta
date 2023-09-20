
import turtle 


def draw_circle(x,y,radius,color):
    '''function should declare the parameters:
    the x and y coordinates where the turtle should begin drawing the circle
    the radius of the circle
    fill_color: the color of the circle
    turtle'''
    turtle.up() #stop drawing
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color) 
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()

def draw_semi_circle(x,y,radius,arc,color):
    turtle.up() #stop drawing
    turtle.goto(x,y)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color) 
    turtle.circle(radius,arc)
    turtle.end_fill()
    turtle.up()

'''def centered_draw_circle():
    turtle.begin_fill()
    turtle.fillcolor("brown")
    turtle.penup() #stop drawing
    turtle.goto(0,50)
    turtle.pendown()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    input("enter to continue...")

def centered_draw_circle_1():
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.penup() #stop drawing
    turtle.goto(0,25)
    turtle.pendown()
    turtle.circle(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    input("enter to continue...")'''


'''def main():
    win=turtle.Screen()
    turta=turtle.Turtle()
    radius=100
    fill_color="blue"
    draw_circle(0,10,radius,fill_color,turta)
    centered_draw_circle(x,y,radius,fill_color,turtle)
    win.exitonclick()

main()'''
draw_circle(120,-310,350,"yellow")
draw_circle(0,0,100,"white")
draw_circle(0,50,50,"brown")
draw_circle(0,75,25,"black")
draw_circle(250,0,100,"white")
draw_circle(250,50,50,"brown")
draw_circle(250,75,25,"black")
draw_circle(125,10,20,"pink")
draw_semi_circle(20,-90,100,180,"red")


turtle.exitonclick()


'''
centered_draw_circle()
centered_draw_circle_1()'''
