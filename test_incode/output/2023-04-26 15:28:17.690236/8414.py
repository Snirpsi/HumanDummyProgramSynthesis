#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and adds numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That is not a number")
            continue
        else:
            print(number + 