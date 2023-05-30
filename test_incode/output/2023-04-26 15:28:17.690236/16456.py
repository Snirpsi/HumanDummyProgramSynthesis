#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and returns fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = []
    
    while True:
        fruits.append(words.pop(0))
        
        if words:
            fruits.append(' ')
            
    print(' '.join(fruits))
    
