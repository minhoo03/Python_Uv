import turtle as t

colors = ['red','purple','blue','green','orange','yellow']
t.setup(500, 400)
t.bgcolor('black')

for i in range(180):
    t.pencolor(colors[i % len(colors)])
    t.width(i/100 +1)
    t.forward(i)
    t.left(59)