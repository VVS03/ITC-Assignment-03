import math
#a
result = (3+4)*(5)
print(result)

#b
n= int(input("enter value of n : "))
expressions = n*(n-1)/2
print(expressions)

#c
r = int(input("enter the value of r : "))
c = 4*math.pi*(r**2)
print(c)

#d
R = int(input("enter the value of R : "))
a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
d = math.sqrt(R*(math.cos(a))**2 + R*(math.sin(b))**2)
print(d)

#e
y1 = int(input("enter the value of y1 : "))
y2 = int(input("enter the value of y2 : "))
x1 = int(input("enter the value of x1 : "))
x2 = int(input("enter the value of x2 : "))

e = (y2-y1)/(x2-x1)
print(e)
