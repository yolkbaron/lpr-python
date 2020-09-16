from random import *
from turtle import *
from numpy import *


number_of_atoms = 5
steps_of_time_number = 2000
size = 100
atomsize = 10

penup()
goto(size, size)
pendown()
goto(size, -size)
goto(-size, -size)
goto(-size, size)
goto(size, size)
penup()
ht()
gas = [Turtle(shape='circle') for i in range(number_of_atoms)]
x = {}
y = {}
vx = {}
vy = {}
for atom in gas:
    atom.penup()
    atom.speed(0)
    atom.left(90)
    x[atom] = randint(-size + atomsize, size - atomsize)
    y[atom] = randint(-size + atomsize, size - atomsize)
    vx[atom] = randint(-size, size)/10
    vy[atom] = randint(-size, size)/10
    atom.shapesize(atomsize/10)
    atom.goto(x[atom], y[atom])

for i in range(steps_of_time_number):
    for atom in gas:
        x[atom] += vx[atom]
        y[atom] += vy[atom]
        if x[atom] > size - atomsize or x[atom] < -size + atomsize:
            x[atom] -= vx[atom]
            vx[atom] = -vx[atom]
        if y[atom] > size - atomsize or y[atom] < -size + atomsize:
            y[atom] -= vy[atom]
            vy[atom] = -vy[atom]
        for atom2 in gas:
            if (x[atom] - x[atom2])**2 + (y[atom] - y[atom2])**2 < 2*atomsize**2:
                vx1 = vx[atom]
                x1 = x[atom]
                vx2 = vx[atom2]
                x2 = vx[atom2]
                vy1 = vy[atom]
                y1 = y[atom]
                vy2 = vy[atom2]
                y2 = vy[atom2]
                d = sqrt((x1-x2)**2+(y1-y2)**2)
                u = -((x1-x2)*(vx1-vx2)/d + (y1-y2)*(vy1-vy2)/d)
                vx[atom] = vx1 + u*(x1-x2)/d
                vx[atom2] = vx2 + u*(x2-x1)/d
                vy[atom2] = vy2 + u*(y2-y1)/d
                vy[atom] = vy1 + u*(y1-y1)/d
        atom.goto(x[atom], y[atom])
done()
