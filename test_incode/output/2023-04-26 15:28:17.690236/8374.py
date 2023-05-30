#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and prints a list of numbers. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    numbers = []
    for word in words:
        numbers.append(word.count('