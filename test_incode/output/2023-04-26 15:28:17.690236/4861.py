#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or removes a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                print(number)
            else:
                print("Number must be greater than 0")
        else:
            print("Enter only numbers")
