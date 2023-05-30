#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = [
        'apple', 'banana', 'cherry', 'date', 'dog', 'elephant', 'fox',
        'goat', 'horse', 'lion', 'monkey', 'orange', 'pig', 'rabbit',
        'sheep', 'tiger', 'whale', 'zebra'
    ]
    
    words.sort()
    
    print('\n'.join(words))
    
