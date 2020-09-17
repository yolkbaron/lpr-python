from random import *
from turtle import *


number_of_atoms = 10
steps_of_time_number = 2000
size = 100 #размер поля
atomsize = 1
quality = 10 #чем больше, тем выше точность одного шага 

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
            x[atom] -= vx[atom]
            vx[atom] = -vx[atom]
        if y[atom] > size - atomsize or y[atom] < -size + atomsize:
            y[atom] -= vy[atom]
            vy[atom] = -vy[atom]
        atom.goto(x[atom], y[atom])
done()
