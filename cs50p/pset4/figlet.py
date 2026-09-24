from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:

    statement = input("Input: ")
    temp=Figlet()
    all_fonts = temp.getFonts()
    chosen = random.choice(all_fonts)
    f=Figlet(font=chosen)
    print(f.renderText(statement))

elif len(sys.argv) == 3:
    statement = input("Input: ")
    temp=Figlet()
    f=Figlet(font=sys.argv[2])
    print(f.renderText(statement))


else: ValueError



