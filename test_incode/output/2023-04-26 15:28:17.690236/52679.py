#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Negative numbers are not allowed")
        elif number == 0:
            print("Zero is not allowed")
        else:
            print(number)
