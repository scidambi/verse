def main():
    count = 0
    items = {item, count}
    while True:
        try:
            item = input("Item: ").upper()
            count = 1 + count
            print(count)
            print(items)
        except: ValueError
        else: continue
main()