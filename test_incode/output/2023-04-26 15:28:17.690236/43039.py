#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers or enumerates a list of words. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for index, num in enumerate(numbers):
        print('{}. {}'.format(index, words[index]))
        
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
        
    print('Done.')
    
