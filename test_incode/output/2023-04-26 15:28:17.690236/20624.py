#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Sorry, that number is negative.")
        elif number == 0:
            print("Sorry, that number is zero.")
        else:
            