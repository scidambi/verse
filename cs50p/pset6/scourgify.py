import sys
import csv

def main():

    if len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit()

    if len(sys.argv) == 2:
        print("Too few arguments")
        sys.exit()

    input = sys.argv[1]
    output = sys.argv[2]  

    if input.endswith(".csv") and output.endswith(".csv"):
        try:
            file = open("before.csv")
            reader = csv.DictReader(file)
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            fieldnames = ['first name', 'last name', 'house']
            writer.writeheader()
            for row in reader:
                print(row['name'].split(",")[0], row['name'].split(",")[1], row ['house'])
            
            file = open("after.csv", mode = "w", newline = "")
        except FileNotFoundError:
            print("File does not exist")
        else:
            print("Not a csv file")


main()


