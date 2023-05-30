#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        choice = input("Would you like to convert your input to a number? y/n: ")
        if choice == 'y':
            number = int(input("Enter a number: "))
            print(number)
        elif choice == 'n':
            break
        else:
            print("Invalid input. Try again.")
