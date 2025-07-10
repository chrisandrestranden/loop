def loop_one():
    while True:
        number = int(input("Loop 1 — Enter a number (0 to go back to menu): "))
        if number == 0:
            print("\nReturning to menu...\n")
            break
        elif number > 5:
            print("\nYour number is bigger than 5.\n")
        elif number == 5:
            print("\nYour number is 5.\n")
        else:
            print("\nYour number is smaller than 5.\n")


def loop_two():
    while True:
        number = int(input("Loop 2 — Enter a number (0 to go back to menu): "))
        if number == 0:
            print("\nReturning to menu...\n")
            break
        elif number % 2 == 0:
            print("\nYour number is even.\n")
        else:
            print("\nYour number is odd.\n")


# --- Main menu loop ---
while True:
    print("Menu:")
    print("1. Run Loop 1")
    print("2. Run Loop 2")
    print("0. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        loop_one()
    elif choice == "2":
        loop_two()
    elif choice == "0":
        print("\nGoodbye!\n")
        break
    else:
        print("\nInvalid option. Try again.\n")
