#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or calculates a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            number = int(number)
            print(number * 