#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or converts a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            print(number)
        except 