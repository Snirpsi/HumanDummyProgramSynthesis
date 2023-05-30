#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or multiplyes a list of words. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0 and number < 10:
                print(number * 10)
            else:
                print("Invalid number")
        else:
            print("Invalid number")
