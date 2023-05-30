#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and converts words. """    
    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    
    print('The words 