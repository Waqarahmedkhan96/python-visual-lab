import turtle
import time

# --- CONFIGURATION ---
RED = "#C8102E"  # Official Danish Red
WHITE = "#FFFFFF"
SPEED = 2        # Animation speed (1-10)

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Waqar: The Birth of the Danish Flag")
    screen.bgcolor("white")
    return screen

def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def animate_flag():
    t = turtle.Turtle()
    t.speed(SPEED)
    t.hideturtle()

    # 1. Drawing the Red Background
    # Standard proportions: 12:12 for the red fields, but we'll use a 37:28 ratio
    draw_rectangle(t, -300, -200, 600, 400, RED)
    
    time.sleep(0.5)

    # 2. Animate the White Vertical Bar
    # Positioned at 12/37ths from the left
    t.penup()
    t.goto(-120, -200)
    t.pendown()
    t.color(WHITE)
    t.width(60) # Width of the cross
    t.setheading(90)
    
    # "Growing" animation
    for _ in range(40):
        t.forward(10)
        
    time.sleep(0.3)

    # 3. Animate the White Horizontal Bar
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.setheading(0)
    
    # "Growing" animation
    for _ in range(60):
        t.forward(10)

    # Final Text
    t.penup()
    t.goto(0, -260)
    t.color("black")
    t.write("Waqar: Made with Python Turtle :)", align="center", font=("Arial", 16, "bold"))

if __name__ == "__main__":
    win = setup_screen()
    animate_flag()
    win.mainloop()