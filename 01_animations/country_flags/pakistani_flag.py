import turtle
import time

# --- CONFIGURATION ---
PAK_GREEN = "#01411C"  # Official Pakistani Green
WHITE = "#FFFFFF"
SPEED = 3

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Sabz Hilali Parcham: Pakistan Flag Animation")
    screen.bgcolor("#111111") # Dark background to make colors pop
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

def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.setheading(50) # Tilted star as per official flag
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def animate_pak_flag():
    t = turtle.Turtle()
    t.speed(SPEED)
    t.hideturtle()

    # 1. Draw the Green Field (3/4 of the flag)
    draw_rectangle(t, -100, -200, 450, 400, PAK_GREEN)
    
    # 2. Draw the White Hoist (1/4 of the flag)
    draw_rectangle(t, -250, -200, 150, 400, WHITE)

    # 3. Animate the Crescent
    # Outer circle (White)
    draw_circle(t, 130, -110, 110, WHITE)
    # Inner circle (Green) to cut the crescent shape
    draw_circle(t, 160, -85, 100, PAK_GREEN)

    # 4. Animate the Star
    draw_star(t, 135, 60, 50, WHITE)

    # Final Text
    t.penup()
    t.goto(0, -260)
    t.color("#FFD700") # Royal Gold text
    t.write("PAKISTAN: Sabz Hilali Parcham", align="center", font=("serif", 20, "bold"))

if __name__ == "__main__":
    win = setup_screen()
    animate_pak_flag()
    win.mainloop()
