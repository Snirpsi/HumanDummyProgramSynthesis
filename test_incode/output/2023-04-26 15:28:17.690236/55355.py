#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That is not a valid number!")
        else:
            print("You entered", number)
