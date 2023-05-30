#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or stores user input. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Invalid number")
        elif number == 0:
            print("Zero")
        else:
            print(number)
