#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits and returns a list of words. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    words = [fruit for fruit in fruits if fruit != 'cherry']
    print(words)
    
