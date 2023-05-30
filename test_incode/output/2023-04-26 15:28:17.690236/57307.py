#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and adds a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        print('The list contains:', end='')
        print(*range(number), sep=', ')
        print('')
        
