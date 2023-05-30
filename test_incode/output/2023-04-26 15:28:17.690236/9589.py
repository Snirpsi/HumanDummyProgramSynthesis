#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or enumerates a list of words. """    
    
    numbers = range(10)
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    print('\n'.join([str(number) for number in numbers if number in words]