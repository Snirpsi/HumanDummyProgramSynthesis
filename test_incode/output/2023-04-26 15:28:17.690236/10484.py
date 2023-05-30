#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or multiplyes a list of numbers. """    
    while True:
        number = input("Enter a number or 0 to quit: ")
        if number == "0":
            break
        else:
            number = int(number)
            if number == 0:
                break
            number = number * 2
            print(number)
    
