#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print("Too high!")
        elif number < 1:
            print("Too low!")
        else:
            print("The number is", number)
