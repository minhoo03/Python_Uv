import turtle as t

cols =['red', 'blue', 'green', 'purple', 'magenta','black','gray','yellow','cyan','orange','aqua']

def drawpolygon(n, size):
    for i in range(n):
        t.pencolor(cols[i % len(cols)])
        t.forward(size)
        t.left(360/n)

t.setup(500, 400)
t.speed(3)


t.pu()
t.goto(-50, -170)

t.pd()

for i in range(3, 12):
    drawpolygon(1, 100)