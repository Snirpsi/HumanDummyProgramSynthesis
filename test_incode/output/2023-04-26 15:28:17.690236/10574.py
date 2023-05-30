#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and returns fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    print('\n'.join(