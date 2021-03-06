from random import *
from turtle import *
from numpy import *


number_of_atoms = 100
steps_of_time_number = 2000
size = 100 #size of field
atomsize = 10
quality = 1 #lowers step size

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
    vx[atom] = randint(-size, size)/quality
    vy[atom] = randint(-size, size)/quality
    atom.shapesize(atomsize/10)
    atom.goto(x[atom], y[atom])

for i in range(steps_of_time_number):
    for atom in gas:
        x[atom] += vx[atom]
        y[atom] += vy[atom]
        if x[atom] > size - atomsize or x[atom] < -size + atomsize: 
            if x[atom] > 0:
                x[atom] = size - atomsize
            else:
                x[atom] = -size + atomsize
            vx[atom] = -vx[atom]
        if y[atom] > size - atomsize or y[atom] < -size + atomsize:
            if y[atom] > 0:
                y[atom] = size - atomsize
            else:
                y[atom] = -size + atomsize
            vy[atom] = -vy[atom]
        for atom2 in gas:
            if (x[atom] - x[atom2])**2 + (y[atom] - y[atom2])**2 <= 4*atomsize**2:
                vx1 = vx[atom]
                x1 = x[atom]
                vx2 = vx[atom2]
                x2 = x[atom2]
                vy1 = vy[atom]
                y1 = y[atom]
                vy2 = vy[atom2]
                y2 = y[atom2]
                d = sqrt((x1-x2)**2+(y1-y2)**2)+1 #distance between atoms
                u = -((x1-x2)*(vx1-vx2)/d + (y1-y2)*(vy1-vy2)/d) #change in the speed of the first atom
                vx[atom] += u*(x1-x2)/d
                vx[atom2] -= u*(x1-x2)/d
                vy[atom] += u*(y1-y2)/d
                vy[atom2] -= u*(y1-y2)/d
        atom.goto(x[atom], y[atom])
done()
