#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    for index, word in enumerate(words):
        print('{}. {}'.format(index, word))
    
