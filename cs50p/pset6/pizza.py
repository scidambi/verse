
import sys
import tabulate 
import csv

def main():

    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()

    if len(sys.argv) == 1:
        print("Too few arguments")
        sys.exit()

    name = sys.argv[1]


    if len(sys.argv) == 2 and name.endswith(".csv"):
        try: 
            file = open(sys.argv[1])
            table = csv.reader(file)
            print(tabulate.tabulate(table, tablefmt="grid", headers="firstrow"))
        except FileNotFoundError:
            print("File does not exist")
    else:
        print("Not a csv file")
    
main()