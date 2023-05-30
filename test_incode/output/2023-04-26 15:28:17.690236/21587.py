#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and enumerates a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
        for number in numbers:
            print('{}. {}'.format(number, word))
