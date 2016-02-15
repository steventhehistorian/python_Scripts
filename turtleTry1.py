import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Maggie Drawing!")      # Set the window title



maggie=turtle.Turtle() # Create a turtle object.
#turtle.tracer(0,0) # Don't watch Turtle draw.
turtle.speed(0)
# Draws 2 squareish things.
##for j in range(1,3):
##      maggie.penup()
##      if j==1:
##            maggie.setposition(-200,0)
##      else:
##            maggie.setposition(200,0)
##      maggie.pendown()
##      for i in range(1,100):
##            if i%2==0:
##                  maggie.pencolor("blue")
##            elif i%2 > 0:
##                  maggie.pencolor("red")
##            maggie.forward(10+i)
##            maggie.right(45)
##            maggie.forward(.3*i)
##            maggie.right(45)


for i in range(-30,30):
      maggie.penup()
      maggie.setposition(i*10,0)
      maggie.pendown()
      for j in range(10):
            maggie.left(145)
            maggie.forward(70)

for i in range(-30,30):
      maggie.penup()
      maggie.setposition(0,i*10)
      maggie.pendown()
      for j in range(5):
            maggie.left(145)
            maggie.forward(70)
for i in range(-30,30):
      maggie.penup()
      maggie.setposition(0,i*5)
      maggie.pendown()
      for j in range(5):
            maggie.right(145)
            maggie.forward(70)
turtle.done() # Pauses the program.  Close window to continue.
turtle.update()
