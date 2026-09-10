def main(): 
    ...
    time = input("What time is it?")
    time = convert(time)
def convert(time):
    x, y = time.split(":")
    x=float(x)
    y=float(y)
    converted_time = float((x + (y/60)))
    if converted_time > 19:
        pass
    elif converted_time >= 18:
        print("Dinner time")
    elif converted_time > 13:
        pass
    elif converted_time >= 12:
        print("Lunch time")
    elif converted_time > 8:
        pass
    elif converted_time >= 7:
        print("Breakfast time")

        



if __name__ == "__main__":
    main()