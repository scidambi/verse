amount = int(input("Amount Due: "))

while amount > 0:
        print("Amount due:", amount)
        coin = int(input("Insert coin: "))
        amount = amount - coin

print("Amount due: ", amount)



