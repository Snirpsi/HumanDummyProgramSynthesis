#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or prints fruits. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            print("That is not a number!")
