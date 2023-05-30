#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            print("Invalid input.")
