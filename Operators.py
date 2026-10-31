'''micro-python script to design a calculator with the following
operators ('+','-','*','/','//','%'). on two input numbers input added by user
'''

from time import sleep as s

print("--CALCULATOR--")
print("available operators are('+','-','*','/','//','%')")
while True:
    a = int(input("Type 1st number: "))
    print(type(a))
    b = int(input("Type 2nd number: "))
    print(type(b))
    sign = input("Type sign (+,-,*,/,//,%): ")
    
    if sign == '+':
        print("add:", a + b)
    elif sign == '-':
        print("sub:", a - b)
    elif sign == '*':
        print("mul:", a * b)
    elif sign == '/':
        if b != 0:
            print("div:", a / b)
        else:
            print("Cannot div by zero")
    elif sign == '//':
        if b != 0:
            print("floor div:", a // b)
        else:
            print("Cannot div by zero")
    elif sign == '%':
        if b != 0:
            print("Percentage:", a % b)
        else:
            print("can't caluculate by ZERO")
    else:
        print("Invalid operator")