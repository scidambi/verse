
def y():
    x = int(input("Enter a number"))
    steps = 0
    while x > 1:
        if x % 2 == 0:
            x = (x/2)
        else:
            x = ((x*3)+1)
        steps = steps + 1
    if x == 1:
        return steps
    if x < 0:
        return("Value Error")

print(y())