import turtle as trtl
import time
import random

#defining variable
screen = trtl.Screen()
#make screen 600x400
screen.setup(600, 400)

# Defines turtle for stoplight
traffic = trtl.Turtle()
traffic.speed(0)
traffic.hideturtle()
# Defines turtle for car
car = trtl
car.speed(0)
car.hideturtle()
# Defines turtle for background
painter = trtl.Turtle()
painter.hideturtle()
painter.speed(0)

counter = 0
turn = 0
light = "green"
# Allows easy changes to stoplight position
light_x = 0
light_y = 70

# Draws a circle of the specified color at the specified coordinates
def light_change(x, y, color):
    traffic.penup()
    traffic.goto(light_x+x, light_y+y)
    traffic.pendown()
    traffic.setheading(315)
    traffic.pencolor(color)
    traffic.fillcolor(color)
    traffic.begin_fill()
    traffic.circle(5, 360)
    traffic.end_fill()

def car_go():
  #different cars
  if turn == 1:
    image = "istockphoto-185257478-612x612-removebg-preview.gif"
    speed = 18
  elif turn == 2:
    image = "image (1).gif"
    speed = 12
  elif turn == 3:
    image = "ezgif-6-8c6b7926f4.gif"
    speed = 16
  else:
    image = "images-removebg-preview.gif"
    speed = 22
  #car gets defined and put at beginning of screen
  car.hideturtle()
  car.penup()
  car.goto(-500, -70)
  screen.addshape(image)
  car.shape(image)
  car.showturtle()
  for i in range(20):
    car.forward(speed)
    time.sleep(.01)
  car.pendown()

# Draws a building with a random size
def draw_building():
 height = random.randint(80,300)
 width = random.randint(80,150) 
 roof = random.randint(1, 1)
 painter.pendown()
 painter.color("#D3D3D3")
 painter.fillcolor("#D3D3D3")
 painter.setheading(90)
 painter.begin_fill()
 painter.forward(height)
 painter.right(90)
 painter.forward(width)
 painter.right(90)
 painter.forward(height)
 painter.right(90)
 painter.forward(width)
 painter.end_fill()
 painter.right(180)
 painter.forward(width)
 painter.penup()

# Draws one side of sidewalk
def draw_sidewalk():
 painter.pendown()
 painter.color("#a9a9a9")
 painter.fillcolor("#a9a9a9")
 painter.begin_fill()
 painter.setheading(90)
 painter.forward(30)
 painter.right(90)
 painter.forward(1000)
 painter.right(90)
 painter.forward(30)
 painter.right(90)
 painter.forward(1000)
 painter.end_fill()

# Sets background
painter.screen.bgcolor("aqua")
# Draws buildings in background
painter.penup()
painter.goto(-500,-10)
for i in range(10):
  painter.forward(10)
  draw_building()
painter.goto(-500,-180)

#gray pavement of the street
painter.pendown()
painter.color("#3f3f3f")
painter.fillcolor("#3f3f3f")
painter.setheading(90)
painter.begin_fill()
painter.forward(150)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(150)
painter.right(90)
painter.forward(1000)
painter.end_fill()

#Yellow lines on the street 
painter.right(90)
painter.forward(75)
painter.color("#f7b500")
painter.fillcolor("#f7b500")
painter.setheading(90)
painter.begin_fill()
painter.forward(13)
painter.right(90)
painter.forward(1000)
painter.right(90)
painter.forward(13)
painter.right(90)
painter.forward(1000)
painter.end_fill()
painter.penup()

# Draws sidewalks
painter.goto(-500,-30)
draw_sidewalk()
painter.goto(-500,-210)
draw_sidewalk()
painter.penup()

# Draws part of stoplight pole that connects to backing
traffic.penup()
traffic.goto(light_x+19, light_y+50)
traffic.pendown()
traffic.setheading(0)
traffic.pencolor("#888888")
traffic.fillcolor("#888888")
traffic.begin_fill()
for i in range(2):
    traffic.forward(30)
    traffic.right(90)
    traffic.forward(10)
    traffic.right(90)
traffic.end_fill()

# Draws part of stoplight pole that connects other parts
traffic.penup()
traffic.goto(light_x+59, light_y+40)
traffic.pendown()
traffic.setheading(90)
traffic.begin_fill()
traffic.circle(10, 180)
traffic.end_fill()

# Draws part of stoplight pole that connects to ground
traffic.penup()
traffic.goto(light_x+59, light_y+40)
traffic.pendown()
traffic.setheading(270)
traffic.begin_fill()
for i in range(2):
    traffic.forward(120)
    traffic.right(90)
    traffic.forward(10)
    traffic.right(90)
traffic.end_fill()

# Draws stoplight backing
traffic.penup()
traffic.goto(light_x-11, light_y+69)
traffic.pendown()
traffic.setheading(0)
traffic.begin_fill()
for i in range(2):
    traffic.forward(30)
    traffic.right(90)
    traffic.forward(50)
    traffic.right(90)
traffic.end_fill()

# Draws unlit lights: red, yellow, and green
light_change(0, 55, "#bb0000")
light_change(0, 40, "#bbbb00")
light_change(0, 25, "#00bb00")

car.showturtle()
turn = 0
# Should loop forever, different cars driving up in the same cycle
while turn <= 4:
  turn += 1
  # Light turns yellow while car drives up to light
  light = "yellow"
  light_change(0, 25, "#00bb00")
  light_change(0, 40, "#ffff00")
  car_go()
  
  #prevent line from trailing after car :(
  car.penup()
  car.speed(0)
  
  # Light turns red while car stops at light
  light = "red"
  light_change(0, 40, "#bbbb00")
  light_change(0, 55, "#ff0000")
  #car wait.
  time.sleep(5)
  
  #move car by delaying .02 second
  if turn == 1:
    speed = 25
  elif turn == 2:
    speed = 20
  elif turn == 3:
    speed = 40
  else:
    speed = 40
    turn = 0
  # Light turns green while car moves
  light = "green"
  light_change(0, 55, "#bb0000")
  light_change(0, 25, "#00ff00")
  for i in range(48):
    car.forward(speed)
    time.sleep(.01)

wn = trtl.Screen()
wn.mainloop()