#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That's not a number!")
        else:
            print(number)
