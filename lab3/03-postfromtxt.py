from turtle import *
from numpy import *

def addnum(num:int):
    inp = open('03-nums.txt', 'r').readlines()
    s = inp[num].rstrip()
    print(s)
    commlist = s.split(' -> ')
    for command in commlist:
        eval(command)


def drawindex(index:float):
    for num in index:
        addnum(int(num))


shape('turtle')
speed(8)
color('blue','blue')
width(3)
left(90)
index = '1234567890'
drawindex(index) 
done()
