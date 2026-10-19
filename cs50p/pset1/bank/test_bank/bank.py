def main():

    greeting = input("Hello Newman")
    greeting = greeting.strip()
    print(value_greeting(greeting))

def value_greeting(greeting):

    result = ""

    
    if greeting == "":
        result = 100
    elif greeting.split()[0] == "hello":
        result = 0
    elif greeting[0] == "h":
        result = 20
    else:
        result = 100

    return(result)


if __name__ == "__main__":
    main()