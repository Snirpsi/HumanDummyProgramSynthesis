#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or converts a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
        else:
            print(number)
