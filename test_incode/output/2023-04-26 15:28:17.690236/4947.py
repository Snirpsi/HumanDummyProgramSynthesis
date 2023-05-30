#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and returns fruits. """    
    
    words = ['apple', 'orange', 'banana', 'pear']
    fruits = ['apple', 'orange']
    
    for word in words:
        for fruit in fruits:
            print(word, fruit)
