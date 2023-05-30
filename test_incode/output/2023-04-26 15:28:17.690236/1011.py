#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or multiplyes fruits. """    
    import sys
    
    fruits = sys.argv[1:]
    
    for fruit in fruits:
        if fruit == '' or fruit == '*':
            continue
        
        fruits.remove(fruit)
        
    for fruit in fruits:
        print(fruit)
        
