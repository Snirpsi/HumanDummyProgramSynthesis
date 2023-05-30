#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or returns a list of words. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('Invalid number')
        else:
            print('The number is', number)
            break
