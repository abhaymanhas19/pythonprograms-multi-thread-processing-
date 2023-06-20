import turtle
from tkinter import Tk, Canvas
from sketchpy import canvas

# Create a Tkinter window
root = Tk()

# Create a canvas to display turtle graphics
screen = turtle.TurtleScreen(Canvas(root))
screen.bgcolor('white')

# Create a turtle object
t = turtle.RawTurtle(screen)

# Load the SVG file using sketchpy
obj = canvas.sketch_from_svg("/home/jarvis/Downloads/12.svg")

# Set up the turtle pen
t.penup()
t.pendown()

# Draw the SVG using the turtle
obj.draw(t)

# Start the Tkinter event loop
root.mainloop()
