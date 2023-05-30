#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or stores a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 999:
            break
        else:
            print(number)
