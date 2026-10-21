def main():
    fraction = input("Fraction:")
    print(convert(fraction))
    print(gauge(convert(fraction)))
       
def convert(fraction):
   
    while True:
        try:
            y = int((fraction.split("/")[0]))/int((fraction.split("/")[1]))*100
        except (ValueError,ZeroDivisionError):
            continue
        else:
            break
    return y

def gauge(y):
    while True:
        try:     
            if y>100:
                continue
            if y <= 1:
                result = "E"
            elif y >= 99:
                result = "F"
            else:
                result = f"{y}%"
        except (ValueError,ZeroDivisionError):
            continue
        else:
            break
    return(result)

if __name__ == "__main__":
    main()


