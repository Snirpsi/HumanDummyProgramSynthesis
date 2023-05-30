#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 1000:
            print("The number is too large.")
        elif number < 1:
            print("The number is too small.")
        else:
            print(number)
