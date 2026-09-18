def main():
    count = 0
    while True:
        try:
            item = input("Item: ").upper()
            count = 1 + count
            print("ji")
        except: ValueError
        else: continue


main()