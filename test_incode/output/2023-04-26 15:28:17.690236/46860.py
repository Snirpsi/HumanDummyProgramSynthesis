#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and multiplyes numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    i = 0
    while i < len(words):
        words[i] = words[i] * numbers[i]
        i += 1
    
    print(' '.join(words))
    
