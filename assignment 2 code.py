#Write a Python program to convert kilometers to miles?
a=float(input("enter your value in Kilometer: "))
b=a/1.609
print("the value in miles is:",b)

# Write a Python program to convert Celsius to Fahrenheit?
celcuis=24
frhenheit=(celcuis*9/5) + 32
print(frhenheit)

# Write a Python program to display calendar?
import calendar
yy=2022
mm=8
print(calendar.month(yy,mm))

# Write a Python program to solve quadratic equation?
from math import sqrt

def quadratic(a, b, c):
    x1=-b/(2*a)
    x2=sqrt(b**2 -4*a*c)/2*a
    return(x1+x2,x1-x2)
quadratic(1,12,32)

#Write a Python program to swap two variables without temp variable
a=10
b=20
a,b=b,a
print(a)
print(b)