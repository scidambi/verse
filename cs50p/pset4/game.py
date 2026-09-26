import random
import sys


def level():
    level = int(input("Level: "))
    return level

n = level()

def answer ():
    answer = int(random.randrange(0, n))
    return answer

secret = answer()

def main():
    while True:
        try:
            guess = int(input("Guess: "))
            if secret > guess:
                print("Cool")
            elif secret < guess:
                print("not cool")
            else: print("perfect")
        except ValueError:
            print("Integer please")



main()
        


