expression = input("Expression:")

x, y, z = expression.split(" ")
x = int(x)
z = int(z)



def multiply(x,z):
    return int(x*z)
def add(x,z):
    return int(x+z)
def subtract(x,z):
    return int(x-z)
def divide(x,z):
    return int(x/z)

if y == "+":
    print(add(x,z))

if y == "-":
    print(subtract(x,z))

if y == "*":
    print(multiply(x,z))

if y == "/":
    print(divide(x,z))

