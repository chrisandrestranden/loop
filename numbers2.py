
#Test-file for GitHub

while True:

    number = int(input("Enter a number (0 to quit): "))

    if number == 0:
        print("\nGoodbye!\n")
        break

    elif number > 5:
        print("\nYour number is bigger than 5.\n")    
    
    elif number == 5:
        print("\nYour number is 5.\n")
    
    else:
        print("\nYour number is smaller than 5.\n")