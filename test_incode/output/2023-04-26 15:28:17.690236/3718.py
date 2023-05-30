#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or prints a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(int(number))
        else:
            print("Invalid input")
