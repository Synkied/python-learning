import turtle

def drawThing(fwd, direction, rng):
	my_turtle = turtle.Turtle()

	for i in range(rng):
		my_turtle.forward(fwd)
		my_turtle.right(direction)

drawThing(100, 90, 4)

# draws a square at position (100,100)
my_square = turtle.Turtle()
my_square.pencolor("red")

my_square.setposition(100,100)
for i in range(4):
	my_square.forward(100)
	my_square.right(90)

my_weirdThing = turtle.Turtle()
my_weirdThing.setposition(-90,-90)

for i in range(50):
	my_weirdThing.forward(50)
	my_weirdThing.left(123)

turtle.done()

