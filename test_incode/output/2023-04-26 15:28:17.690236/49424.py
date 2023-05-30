#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or opens a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            print("Invalid input. Try again.")
