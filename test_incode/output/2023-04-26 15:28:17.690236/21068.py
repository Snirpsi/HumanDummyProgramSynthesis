#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and prints a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        print('\nFruits:')
        for fruit in fruits:
            print('\t' + fruit)
        
        print('\nPress enter to exit.')
        
        input()
        
