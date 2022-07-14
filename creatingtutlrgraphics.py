import turtle
colors=['red','purple','white','green','orange','yellow']
t=turtle.Pen()
turtle.bgcolor('grey')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+4)
    t.forward(x)
    t.left(69)