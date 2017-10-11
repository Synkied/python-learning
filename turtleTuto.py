from turtle import *

def drawThing(fwd, direction, rng):
	my_turtle = Turtle()

	for i in range(rng):
		my_turtle.forward(fwd)
		my_turtle.right(direction)

drawThing(100, 90, 4)

# draws a square at position (100,100)
my_square = Turtle()
my_square.pencolor("red")

my_square.setposition(100,100)
for i in range(4):
	my_square.forward(100)
	my_square.right(90)

my_weirdThing = Turtle()
my_weirdThing.setposition(-90,-90)

for i in range(50):
	my_weirdThing.forward(50)
	my_weirdThing.left(123)


color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()



    
import turtle

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


def make_square(t, sz):
	for _ in range(4):
		t.forward(sz)
		t.left(90)

def make_mov_square(t, sz, r):
	for _ in range(r):
		make_square(t, sz)
		t.penup()
		t.forward(50)
		t.pendown()

def make_inn_square(t, sz, r):
	for _ in range(r):
		make_square(t, sz)
		sz += 20
		t.penup()
		t.right(135)
		t.forward(13.5)
		t.left(135)
		t.pendown()

def draw_poly(t, n, sz):
	for _ in range(n):
		t.forward(sz)
		t.left(45)




tess = make_turtle("hotpink", 2)

# make_inn_square(tess, 20, 5)

draw_poly(tess, 8, 50)

# make_mov_square(tess, 20, 5)

# for _ in range(4):
# 	for i in range(4):
# 		tess.pendown()
# 		tess.forward(100)
# 		tess.left(90)
# 	tess.penup()	
# 	tess.left(45)
# 	tess.forward(10)
# 	tess.right(45)
# 	tess.forward(10)