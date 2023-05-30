#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers or converts numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That is not a number!")
        else:
            print(number)
