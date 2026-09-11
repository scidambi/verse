camelcase = input("camelCase: ")
result = ""

for x in camelcase:
    if x.isupper():
        result = result + "_" + x.lower()
    else:
        result = result + x

print(result)


