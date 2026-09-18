def main():
        while True:
            x = input("Fraction:")
            try:     
                y = int((x.split("/")[0]))/int((x.split("/")[1]))
                if y>1:
                    continue
                if y < 0.01:
                    print("E")
                elif y > 0.99:
                    print("F")
                else:
                     print(f"{round(y*100)}%")
            except (ValueError,ZeroDivisionError):
                continue
            else:
                break


main()


