import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0) # Set to maximum speed (0 is fastest in Turtle)

# --- BONUS: ADD STARS! ---
t.color("white")
for i in range(20):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.penup()
    t.goto(x, y)
    t.pendown()

    size = random.randint(2, 8)
    for i in range(5):
        t.forward(size)
        t.backward(size)
        t.left(72)

# --- MAIN FIREWORKS ---
# We use a loop of 10 to create multiple bursts
for i in range(10):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Generate random RGB colors for each firework
    # Note: Ensure turtle is in 255 colormode for these values
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)
    
    size = random.randint(30, 200)
    
    # This loop draws 36 lines to create a full circle (360 degrees)
    for i in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)

t.hideturtle()
turtle.done()