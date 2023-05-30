#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits and enumerates a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        for word in words:
            print(word, fruit)
