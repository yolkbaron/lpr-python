import turtle as t

t.shape('turtle')
t.speed(1)
t.forward(5)
t.left(90)
for i in range(50):
    t.forward(10 + 5*i)
    t.left(90)
    t.forward(10 + 5*i)
    t.left(90)
     
