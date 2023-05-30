#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or returns fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
        
        fruits = []
        for fruit in ['apple', 'banana', 'orange']:
            fruits.append(fruit)
        
        