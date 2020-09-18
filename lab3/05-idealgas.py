from random import *
from turtle import *


number_of_atoms = 10
steps_of_time_number = 2000

size = 300 
atomsize = 10
quality = 10 

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
    atom.shapesize(atomsize)
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
        atom.goto(x[atom], y[atom])
done()
