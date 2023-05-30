#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = float(number)
        except ValueError:
            print("Invalid input.")
        else:
            print("The number is", number)
