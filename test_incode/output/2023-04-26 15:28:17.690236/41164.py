#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        try:
            i = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
    
    print("You entered 