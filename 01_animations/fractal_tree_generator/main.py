import turtle as tu

# Setup the screen and turtle position
screen = tu.Screen()
screen.bgcolor("black")
tu.left(90) # Point the turtle upwards to start the trunk
tu.penup()
tu.goto(0, -200) # Move to the bottom of the screen
tu.pendown()
tu.speed(0) # Fastest speed

# --- My EXTRACTED CODE START ---
tu.color("brown")  # setting the color of turtle to brown as we are drawing tree
# we will use here recursion function to draw the tree
def tree(i):
    if i < 10:
        return
        # this is base condition to stop recursion bcz if we don't give this base condition turtle will draw it
        # infinite times as this loop recursion loop is infinite until some base condition is not given
    else:
        tu.forward(i)  # we will move our tree in forward dir
        tu.color("orange")  # after it has drawn that straight line we wil make a fruit or flower of orange color
        # which will be circle
        tu.circle(2)
        # after the flower or fruit is drawn we want our color back to brown as we want to draw branch
        tu.color("brown")
        # till here it is drawn this much
        # now we want to draw it is left direction
        tu.left(30)  # so when it goes to Left it will again draw flowe and it will go on till the value of i
        # becomes less than 10
        tree(3*i/4)  # 3*100/4 = 75 now value of i is 75 again 3*75/4 = 56.5 now value of i is 56.5 again 56.5*3/4
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)

tree(100)
# --- My EXTRACTED CODE END ---

tu.done()