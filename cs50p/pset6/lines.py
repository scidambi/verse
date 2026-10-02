import sys

def main():

    if len(sys.argv) == 1:
        print("Not enough arguments")
        sys.exit()
    
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()
    
    name = sys.argv[1]

    if len(sys.argv) == 2 and name.endswith(".py"):
        try: 
            file = open(sys.argv[1])
            line_count = 0
            for line in file:
                stripped = line.strip()
                if stripped.startswith("#") or stripped == "":
                    line_count += 0
                else:
                    line_count += 1
            print(line_count)
        except FileNotFoundError:
            print("File does not exist")
    else:
        print("Not a python file")
    
main()



