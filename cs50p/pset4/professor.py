
import random

def main():
    n = get_level()
    generate_integer(n)   
    

def get_level():
    level = int(input("Level: "))
    if level == 1 or level == 2 or level == 3:
        return level
    else: print("EEE")

#need to add that can only add level 1, 2 or 3


def generate_integer(level):
    if level == 1:
        x = int(random.randrange(0, 10))
        y = int(random.randrange(0, 10))
        sum = int(x+y)
        print(f"X + Y = {x} + {y} = ")
        answer = int(input("answer:"))
        if answer == sum:
            generate_integer(level)
        else: 
            print("EEE")
            generate_integer(level)
    elif level == 2:
        x = int(random.randrange(10, 100))
        y = int(random.randrange(10, 100))
        sum = int(x+y)
        print(f"X + Y = {x} + {y} = ")
        answer = int(input("answer:"))
        if answer == sum:
            generate_integer(level)
        else: 
            print("EEE")
            generate_integer(level)
    elif level == 3:
        x = int(random.randrange(100, 1000))
        y = int(random.randrange(100, 1000))
        sum = int(x+y)
        print(f"X + Y = {x} + {y} = ")
        answer = int(input("answer:"))
        if answer == sum:
            generate_integer(level)
        else: 
            print("EEE")
            generate_integer(level)
    else: print("Na") 

   

#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).


if __name__ == "__main__":
    main()