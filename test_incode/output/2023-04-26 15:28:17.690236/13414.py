#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or stores a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(number * 