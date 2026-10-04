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
            infile = open(input)
            outfile = open(output, mode = "w", newline = "")
            reader = csv.DictReader(infile)
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                print(row['name'].split(",")[0], row['name'].split(",")[1], row['house'])
                last, first = row["name"].split(", ")
                house = row['house']
                writer.writerow({"first": first,"last": last,"house": house})
        except FileNotFoundError:
            print("File does not exist")
        else:
            print("Not a csv file")
main()


