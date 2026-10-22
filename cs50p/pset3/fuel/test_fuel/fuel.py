
def main():
    while True:
        try:
            fraction = input("Fraction:")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
   
    if "/" not in fraction:
        raise ValueError

    y = round(int((fraction.split("/")[0]))/int((fraction.split("/")[1]))*100)
    if y <= 100:
        return y
    raise ValueError

def gauge(y):    
    if y>100:
        raise ValueError
    if y <= 1:
        result = "E"
    elif y >= 99:
        result = "F"
    else:
        result = f"{y}%"
    return(result)

if __name__ == "__main__":
    main()


