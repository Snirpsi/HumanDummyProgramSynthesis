#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and adds fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    for word in words:
        for fruit in fruits:
            print(word + ' ' + fruit)
    
