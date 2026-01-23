import turtle
drawing_screen = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exercise 1: Hexagon    hints: num_side = 6   exterior_angle = 360 / num_sides

alex.clear() # For cleanring the previous examples
alex.up()
alex.goto(0, 0) # Go to the center
alex.down()  # If we dont use the .down after using .up drawing is not possible

side_length = 100
num_sides = 6
exterior_angle = 360 / num_sides

for _ in range(6):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exercise 2: rainbow

alex.clear()

num_circles = 7
rainbow_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

radius = 30
radius_increase = 10
alex.clear()
alex.speed(5)
alex.pensize(11)
alex.up()

for color in rainbow_colors:
    new_radius = radius_increase + radius
    alex.setheading(90)        # to make the alex face up
    alex.goto(new_radius, 0)      # start at bottom of arc
    alex.color(color)
    alex.down()
    alex.circle(radius, 180)   # draw right-opening arc
    alex.up()
    radius += radius_increase # to move alex 10 pixel to right to make it not mixing with other colors

alex.shape("blank")
drawing_screen.exitonclick()

# I made new_radius because each time it goes little bit to sidde that it doesn't mix with other colors
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------