import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Stopclock")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the turtle for displaying time
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0, 0)

# Function to display time
def display_time(seconds):
    pen.clear()
    pen.write(f"Time: {seconds} seconds", align="center", font=("Courier", 24, "normal"))

# Main function to run the stopclock
def stopclock():
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        display_time(elapsed_time)
        time.sleep(1)

# Run the stopclock
stopclock()

# Keep the window open
turtle.mainloop()