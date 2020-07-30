
coins = 0


while True:
    print(f"You have {coins} coins.")
    another = input("Do you want another? ")
    if another.lower() == "yes":
        coins += 1
    elif another.lower() == "no":
        print("Bye!")
        break
    else:
        print("Say yes or no")
