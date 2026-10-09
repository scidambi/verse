import sys
from PIL import Image, ImageOps
import os



def main():

    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if len(sys.argv) <= 2:
        sys.exit("Too few arguments")

    input = sys.argv[1]
    output = sys.argv[2]

    if os.path.splitext(input)[1] == ".jpg" or os.path.splitext(input)[1] == ".jpeg" or os.path.splitext(input)[1] == ".png":
        if os.path.splitext(input)[1] == os.path.splitext(output)[1]:
            try:
                shirt = Image.open("shirt.png")
                user = Image.open(input)
                size = shirt.size
                user = ImageOps.fit(user, size)
                user.paste(shirt, shirt)
                user.save(output)
            except FileNotFoundError:
               sys.exit("File not found")
        else: 
            sys.exit("Wrong file extension")
    else: 
        sys.exit("Wrong file extension")


main()  
    

    



#Open the input with Image.open
#resize and crop the input with ImageOps.fit
    #using default values for method, bleed, and centering
    #overlay the shirt with Image.paste 
    #and save the result with Image.save

