#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and enumerates a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, word in enumerate(words):
        print('{}. {}'.format(index + 1, word))
        for index, num in enumerate(numbers):
            print('{}. {}'.format(index + 1, num))
            
