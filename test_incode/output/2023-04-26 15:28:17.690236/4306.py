#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and iterates over fruits. """    
    
    words = []
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        words.append(fruit)
    
    print('\n'.join(words))
    
