#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print("The number you entered is too high.")
        elif number < 1:
            print("The number you entered is too low.")
        else:
            print(number)
