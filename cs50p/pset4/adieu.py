
def main():

    family = []
    def fragment():
        while True:
            try:
                name = input("Name: ")
                family.append(name)
            except EOFError:
                break
            else: continue
                

    fragment()
    if len(family) == 1:
        print(f"Adieu, Adieu, to {family[0]}")
    elif len(family) == 2:
        print(f"Adieu, Adieu, to {family[0]} and {family[1]}")
    elif len(family) > 2:
        print(f"Adieu, Adieu, to {", ".join(family[:-1])}, and {family[-1]}")
        


main()
