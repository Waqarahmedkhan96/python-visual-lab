import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("Bouncing Shapes")
win.tracer(0)

balls = []
# Use a dictionary to store velocities for each ball
ball_data = []

for _ in range(10):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color(random.choice(["red", "blue", "green", "yellow", "purple"]))
    ball.penup()
    ball.goto(random.randint(-200, 200), random.randint(-200, 200))
    
    # Store the ball and its velocity together in a small dictionary
    ball_data.append({
        "obj": ball,
        "dx": random.randint(2, 5),
        "dy": random.randint(2, 5)
    })

while True:
    win.update()
    for item in ball_data:
        ball = item["obj"]
        
        # Move the ball
        ball.setx(ball.xcor() + item["dx"])
        ball.sety(ball.ycor() + item["dy"])
        
        # Wall Collisions
        if ball.xcor() > 290 or ball.xcor() < -290:
            item["dx"] *= -1
        if ball.ycor() > 290 or ball.ycor() < -290:
            item["dy"] *= -1