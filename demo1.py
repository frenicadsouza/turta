import turtle
#create a turtle control
win=turtle.Screen() #create a graphic windows as win
win.title("my first title") #giving the title as first window
win.bgcolor("light blue") #changing the color of the window

#window is ready, create a turtle to control
turta=turtle.Turtle() #naming the turtle turta
turta.color("black") #make turta red-default color is black
turta.pensize(4) #set the width as 4
turta.pencolor("yellow") #pencolor is yellow
turta.speed(1) #speed is set to 1 (lowest). 10 is fastest

#draw around using the turtle noodles
#1 forward(distance)-moves the turtle forward by a specific distance
turta.forward(200) #turta.fd(200)
#2 backward(distance)- moves turta backward by a specific number of units(distance)
#turta.backward(100)
#3 right- turns thee turtle clockwise
#turta.right(90)
#turta.forward(200)
#turta.right(90)
#turta.forward(200)
#turta.right(90)
#turta.forward(200)

#4 left(angle)- turns the turtle anticlockwise
#turta.left(90)
#turta.forward(200)
#turta.left(90)
#turta.forward(200)
#turta.left(90)
#turta.forward(200)
#5 penup-picks the pen up
turta.left(90)
turtle.penup() #same as turta.up()
turta.forward(200)

#6 pendown/ down()- puts the pen down
turta.left(90)
turta.pendown() #turta.down()
turta.forward(200)

#7 goto(x,y)
turta.goto(10,100)
turta.forward(200)

turta.home() # turtle to the center point-home
turta.setheading(100) #
turta.circle(30) #draws a circle
turta.dot(50)
turta.begin_fill()

turtle.done() # same as win.exitonclick()
#win.bye() #display my window