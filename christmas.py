#imports
import turtle
import random
import time

# this makes the globe


turtle.speed(0)
turtle.penup()
turtle.goto(0,250)
turtle.left(180)
turtle.pendown()
turtle.color("white")
turtle.pensize(15)
turtle.circle(250)
turtle.color("black")
turtle.pensize(10)
turtle.circle(250)
turtle.penup()
turtle.showturtle()
turtle.goto(0,-150)
turtle.circle(50,4)
def make_box():
    turtle.pendown()
    turtle.goto(-100,-150)
    turtle.left(180)
turtle.setheading(-180)
turtle.showturtle()
turtle.goto(400,400)
turtle.pendown()
turtle.pensize(15)
turtle.color("white")
for line in range(2):
    for line in range(4):
        turtle.forward(800)
        turtle.left(90)
    turtle.color("black")
    turtle.pensize(10)



#sets the variable as true for the if statements
snow = True

#it configures the snow turtles
if snow:
    i_scale = 1.5
    snow_size = 4
    snow_speed = 3
    draw_speed = 10
    rate_of_snow_balls = 6
else:
    i_scale = 1
    snow_size = 7
    snow_speed = 2
    draw_speed = 10
    rate_of_snow_balls = 2

width = 600 / i_scale
height = 600 / i_scale

#creates a turtle screen
screen = turtle.Screen()
if not snow:
    screen.setup(width, height)

#the def for the tree
def make_triangle(x, y, size, outline, triangle):
    triangle.hideturtle()
    triangle.penup()
    triangle.setposition(x, y)
    triangle.pensize(3)
    if outline:
        triangle.pendown()
    if not outline:
        triangle.fillcolor("forest green")
        triangle.begin_fill()
    triangle.setposition(x + size, y - size)
    triangle.setposition(x - size, y - size)
    triangle.setposition(x, y)
    if not outline:
        triangle.end_fill()

# def for the balls
def make_ball(x, y, size, colour, ball):
    ball.hideturtle()
    ball.penup()
    ball.setposition(x, y)
    ball.color(colour)
    ball.dot(size)

#def for the moving snow
def move_snow(snow):
    position = snow.position()
    snow.clear()
    make_ball(position[0], position[1] - snow_speed, snow_size, "white", snow)

# randomizes snow fall
def snow_fall():
    rand_make_snow = random.randint(0, rate_of_snow_balls)
    if rand_make_snow == 0:
        snow = turtle.Turtle()
        snow.hideturtle()
        snow.penup()
        list_of_snow.append(snow)
        make_ball(random.randint(-width / 2, width / 2), width / 2, snow_size,
                "white", snow)
    for snow in list_of_snow:
        move_snow(snow)
        if snow.position()[1] <= -width / 2:
            snow.clear()
            list_of_snow.remove(snow)
            del snow
    screen.update()


# make tree 
triangle_1 = turtle.Turtle()
triangle_1.speed(draw_speed)
outline = True
for repeat in range(2):
    make_triangle(0, width / 3, width / 6, outline, triangle_1)
    make_triangle(0, width / 4, width / 4, outline, triangle_1)
    make_triangle(0, width / 8, width / 3, outline, triangle_1)

    outline = False

#updates screen
screen.tracer(0)
stem = turtle.Turtle()
# white snowy ground
stem.penup()
stem.hideturtle()
stem.setposition(-width, -width / 3)
stem.color("white")
stem.begin_fill()
stem.setposition(width, -width / 3)
stem.setposition(width, -width / 2)
stem.setposition(-width, -width / 2)
stem.end_fill()
screen.update()

# tree stem
stem.color("brown")
stem.setposition(-width / 30, -width / 4.8)
screen.tracer(1)
stem.pendown()
stem.begin_fill()
stem.setposition(width / 30, -width / 4.8)
stem.setposition(width / 30, -3 * width / 8)
stem.setposition(-width / 30, -3 * width / 8)
stem.setposition(-width / 30, -width / 4.8)
stem.end_fill()

# sets baground coler
screen.bgcolor("sky blue")

box = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('box.gif')
box.shape('box.gif')
box.penup()
box.speed(0)
box.goto(-155,-215)

box_2 = turtle.Turtle()
box_2.penup()
box_2.shape('box.gif')
box_2.speed(0)
box_2.goto(-155,-180)

box_3 = turtle.Turtle()
box_3.penup()
box_3.shape('box.gif')
box_3.goto(0,-215)

box_4 = turtle.Turtle()
box_4.penup()
box_4.shape('box.gif')
box_4.goto(0,-180)

box_5 = turtle.Turtle()
box_5.penup()
box_5.shape('box.gif')
box_5.goto(155,-215)

box_6 = turtle.Turtle()
box_6.penup()
box_6.shape('box.gif')
box_6.goto(155,-180)

stem.color("white")
stem.pensize(15)
stem.penup()
stem.goto(-240,-135)
for line in range(2):

    stem.pendown()
    stem.pendown()
    stem.begin_fill
    stem.forward(480)
    stem.right(90)
    stem.forward(125)
    stem.right(90)
    stem.forward(480)
    stem.right(90)
    stem.forward(125)
    stem.color("black")
    stem.pensize(10)
    stem.left(270)

text_1 = turtle.Turtle()
text_1.hideturtle()
text_1.penup()  

grinch = turtle.Turtle()
wn.addshape('grinch.gif')
grinch.shape('grinch.gif')
grinch.speed(1)
text_1.setposition(0, width / 2.7)
text_1.color("red")
text_1.write("spam space to make the grinch go to space. Plese don't hold it down.",
    font=("Arial", max(int(30 / i_scale), 15), "bold"),
    align="center")

timer = turtle.Turtle()
timer.penup()
timer.hideturtle()
grinch_x=0
grinch.left(180)
def space_bar():
    grinch.right(90)
    grinch.forward(10)
    grinch.left(90)
    grinch.penup()
    grinch.forward(10)
    grinch.speed(0)
    text_1.clear()
    grinch_x = grinch.xcor()
    
    if grinch_x < -abs(width):
        text_1.write("nice job destroying the grinch. Now go to terminal",
            font=("Arial", max(int(30 / i_scale), 15), "bold"),
            align="center")
        timer.speed(1)
        timer.goto(1000,1000)
       
wn.onkeypress(space_bar, "space")

wn.listen()

# decorations: balls
screen.tracer(2)
ball_colours = ["red", "blue", "green", "yellow", "white", "purple"]

x = int(input("do you want black and whte balls, type 1 for YES, or 2 for NO"))

while x == 2:
    text_1.clear()
    text_1.write("Merry, Merry Christmas",
        font=("Arial", max(int(30 / i_scale), 15), "bold"),
        align="center")

    ball_positions = [(-width / 30, width / 4), (3 * width / 40, width / 5),
        (-width / 20, width / 6), (width / 30, width / 9),
        (-width / 12, width / 30), (width / 12, width / 24),
        (-width / 9, -width / 20), (width / 8, -width / 15),
        (0, -width / 6), (-width / 6, -width / 6),
        (width / 5, -width / 7.5)
        ]
    for position in ball_positions:
        make_ball(position[0], position[1], 20 / i_scale,
            random.choice(ball_colours),
            turtle.Turtle())
    screen.update()

#lights

def make_light(x, y, size, colour, light):
    light.hideturtle()
    light.penup()
    light.setposition(x, y)
    light.color(colour)
    light.dot(size)

screen.tracer(2)
light_colours = ["gold", "white", "gold", "white", "gold", "white"]
light_positions = [(-width / 30, width / 4), (3 * width / 40, width / 5),
    (-width / 20, width / 6), (width / 30, width / 9),
    (-width / 12, width / 30), (width / 12, width / 24),
    (-width / 9, -width / 20), (width / 8, -width / 15),
    (0, -width / 6), (-width / 6, -width / 6),
    (width / 5, -width / 7.5)
    ]
for position in light_positions:
    make_light(position[0], position[1], 20 / i_scale,
        random.choice(light_colours),
        turtle.Turtle())
    screen.update()

# snow is falling…
list_of_snow = []

screen.tracer(0)
for _ in range(50):
    snow_fall()

text_1.setposition(0, width / 2.7)
text_1.color("red")
# text_1.write("Merry Christmas", font=("Georgia", 30, "bold"), align="center")
text_1.clear()
text_1.write("Merry, Merry Christmas",
    font=("Arial", max(int(30 / i_scale), 15), "bold"),
    align="center")

for _ in range(25):
    snow_fall()

text_1.setposition(width / 60, -width / 2.18)
text_1.color("black")
# text_1.write("from", font=("Georgia", 20, "normal"), align="center")

if snow:
    text_1.setposition(width / 6, -width / 2.14)
else:
    text_1.setposition(width / 7.5, -width / 2.14)
text_1.color("forest green")

if snow:
    for _ in range(200):
        snow_fall()
else:        
    while True:
        snow_fall()

turtle.done()