#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or enumerates a list of words. """    
    
    numbers = range(10)
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for number, word in zip(numbers, words):
        print('{} {}'.format(number, word))
    
