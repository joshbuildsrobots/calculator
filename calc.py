import cmath

formula = input("which formula would you like to use?")

def add():
    a = int(input("first num"))
    b = int(input("second num"))
    print(a + b)

def subtract():
    a = int(input("first num"))
    b = int(input("second num"))
    print(a - b)

def multiply():
    a = int(input("first num"))
    b = int(input("second num"))
    print(a * b)

def divide():
    a = int(input("first num"))
    b = int(input("second num"))
    print(a / b)

def quadratic():
    a = int(input("first num"))
    b = int(input("second num"))
    c = int(input("third number"))



    d = (b**2) - (4*a*c)    
    x1 = (-b-cmath.sqrt(d))/(2*a)  
    x2 = (-b+cmath.sqrt(d))/(2*a)  
    print(f'the solutions are {x1} and {x2}') 

if formula == "add":
    add()
elif formula == "subtract":
    subtract()
elif formula == "multiply":
    multiply()
elif formula == "divide":
    divide()
elif formula == "quadratic":
    quadratic()