#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        print("Welcome to the endless loop.")
        print("Enter a number to continue.")
        number = int(input("Enter a number to continue: "))
        if number == -1:
            print("Goodbye!")
            break
        else:
            print("You entered 