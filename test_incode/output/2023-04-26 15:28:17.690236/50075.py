#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or iterates over words. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number.')
        else:
            print(number)
