usertext = input("Input:")
result = ""


for char in usertext:
    if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "o" or char == "O" or char == "u" or char == "U":
        pass
    else:
        result = result + char
    
print(result)