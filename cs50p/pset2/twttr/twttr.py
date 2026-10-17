
def main():

    word = input("Input:")
    print(shorten(word))

def shorten(word):
    result = ""
    for char in word:
        if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "o" or char == "O" or char == "u" or char == "U":
            pass
        else:
            result = result + char
        
    return(result)

    
if __name__ == "__main__":
    main()