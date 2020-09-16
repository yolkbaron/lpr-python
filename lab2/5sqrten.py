import turtle as t

def sqr(a):
    t.penup()
    t.forward(a//2)
    t.pendown()
    t.left(90)
    t.forward(a//2)
    t.left(90)
    for i in range(3):
        t.forward(a)
        t.left(90)
    t.forward(a/2)
    t.penup()
    t.left(90)
    t.forward(a//2)
    t.left(180)
    t.pendown()

t.shape('turtle')
t.speed(10)
for i in range(10):
    sqr(10 + 10*i)
t.done()
