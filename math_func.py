'''
micro-python script to make a calculator using only math module functions.

'''

from time import sleep as s
import math

print("--MATH CALCULATOR--")
print("Available functions are ('sqrt', 'sin', 'cos', 'tan', 'log')")

while True:
    sign = input("Type function (sqrt, sin, cos, tan, log): ")
    
    if sign == 'sqrt':
        a = float(input("Type the number: "))
        if a >= 0:
            print("square root:", math.sqrt(a))
        else:
            print("Can't calculate square root of a -int")
    elif sign == 'sin':
        a = float(input("Type the number: "))
        print("sine:", math.sin(a))
    elif sign == 'cos':
        a = float(input("Type the number: "))
        print("cosine:", math.cos(a))
    elif sign == 'tan':
        a = float(input("Type the number: "))
        print("tangent:", math.tan(a))
    elif sign == 'log':
        a = float(input("Type the number: "))
        if a > 0:
            print("logarithm:", math.log(a))
        else:
            print("Can't calculate log(0) or a -int")
    else:
        print("Invalid math function")