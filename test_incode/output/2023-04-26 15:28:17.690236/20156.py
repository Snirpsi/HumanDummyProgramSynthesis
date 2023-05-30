#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(number, "is a perfect square")
        else:
            print(number, "is a square of 