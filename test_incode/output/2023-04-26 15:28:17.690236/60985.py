#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or prints a list of words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for number, word in enumerate(numbers, start=1):
        print('{}. {}'.format(number, word))
        
    for number, word in enumerate(words, start=1):
        print('{}. {}'.format(number, word))
        
    print('Done')
    
