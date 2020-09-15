import turtle as t

t.shape('turtle')
t.speed(10)
n = int(input())
t.right(360/n)
for i in range(n):
    t.forward(200)
    t.stamp()
    t.goto(0, 0)
    t.right(360/n)
     
