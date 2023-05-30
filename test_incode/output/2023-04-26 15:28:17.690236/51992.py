#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = []
    
    while True:
        words.append(input('Enter a word: '))
        
        if words[-1] == 'q':
            break
        
        print('