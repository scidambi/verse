def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print ("Valid")
    else:
        print("Invalid")
    
    print(plate.punctuation())

    
def is_valid(plate):
    
    if not (2 <= len(plate) <= 6):
        return False
    if not plate[0].isalpha() and plate[1].isalpha():
        return False
    if not plate.isalnum():
        return False
    if not numbers_at_end(plate):
        return False
    return True
    

def numbers_at_end(plate):
     seen_digit = False
     for char in plate:
          if char.isdigit():
               if not seen_digit and char == "0": 
                    return False
               seen_digit = True
          else:
            if seen_digit:
                return False
            
     return True
               
    


main()

