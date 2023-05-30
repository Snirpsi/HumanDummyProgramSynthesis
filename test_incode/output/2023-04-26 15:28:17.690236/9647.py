#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and stores a list of numbers. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant', 'lion', 'tiger', 'zebra']
    numbers = []
    
    for word in words:
        numbers.append(word.count('