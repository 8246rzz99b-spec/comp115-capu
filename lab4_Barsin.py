import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(100)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 1:

def draw_circles(t, size, decrease): #added a decrease variable that you dont need 4 functions
  for _ in range(4):
    t.circle(size)
    size -= decrease

draw_circles(t, 100, 10)

t.clear()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 2:

def draw_special(t, size, repeat):
  for _ in range(repeat): 
    draw_circles(t, size, repeat)
    t.right(360 / repeat)

draw_special(t, 100, 10)

t.clear()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3:

def draw_picture_nice():
    t = turtle.Turtle()
    t.speed(0)

    colors = ['white', 'yellow', 'blue', 'orange', 'red']
    decrease_amounts = [4, 5, 10, 19, 20]

    for i in range(len(colors)):
        t.color(colors[i])
        draw_circles(t, 100, decrease_amounts[i])  # use decrease here
        draw_special(t, 100, 10) 


if __name__ == "__main__":
    drawing_screen = turtle.Screen()
    drawing_screen.bgcolor('black')
    draw_picture_nice()
    drawing_screen.mainloop() # Wait for the user to close the drawing screen


wn.mainloop()