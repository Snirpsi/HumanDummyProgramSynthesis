#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and removes a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    fruits.extend(words)
    fruits = list(set(f