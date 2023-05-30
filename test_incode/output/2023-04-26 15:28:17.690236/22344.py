#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        numbers = [int(n) for n in number.split()]
        numbers = numbers * len(numbers)
        print(' '.join(map(str, numbers)))
        
