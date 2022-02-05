import random

Options = ["a","b","c"]
def sep():
    print("___")
def sepline():
    print("___\n")

print("6 Sided Dice Simulator--\n")

dice = input("Choose # of Dice: ")

while True:
    while True:
        try:
            if int(dice) >= 1:
                break
        except:
            print("***Input Numerical Value***")
            dice = input("Choose # of Dice: ")
            continue
    while True:
        try:
            sep()
            print("You rolled...")
            for x in range(int(dice)):
                print(random.randint(1,6))
            sepline()
            break
        except ValueError:
            print("***Input Numerical Value***")
            sep()
            continue

    prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?:"))

    if prompt == "a":
        continue
    elif prompt == "b":
        sep()
        dice = input("Choose # of Dice: ")
        continue
    elif prompt == "c":
        sep()
        print("Thanks for playing!")
        break
    else:
        print("\n***Please choose one of the following options***")
        sep()
        prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?: "))
        while True:
            if prompt == "a":
                break
            elif prompt == "b":
                sep()
                dice = input("Choose # of Dice: ")
                break
            elif prompt == "c":
                sep()
                print("Thanks for playing!")
                break
            else:
                print("\n***Please choose one of the following options***")
                sep()
                prompt = str(input("(a) Roll Again\n(b) Change # of Dice\n(c) Exit Program\n\nWhat next?: "))
                continue
        if prompt == "a":
            continue
        elif prompt == "b":
            sep()
            dice = input("Choose # of Dice: ")
            continue
        elif prompt == "c":
            sep()
            print("Thanks for playing!")
            break
