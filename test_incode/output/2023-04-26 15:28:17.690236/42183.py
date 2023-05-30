#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and enumerates a list of words. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for number, word in enumerate(numbers, 1):
        print('{} {}'.format(number, word))
    
