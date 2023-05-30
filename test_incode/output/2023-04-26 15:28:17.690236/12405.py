#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and prints a list of words. """    
    
    import sys
    
    fruits = ['apple', 'banana', 'cherry']
    
    words = []
    
    for fruit in fruits:
        words.append(fruit)
    
    print('\n'.join(words))
    
