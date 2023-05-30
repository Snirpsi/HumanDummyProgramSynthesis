#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and enumerates a list of numbers. """    
    
    numbers = enumerate( range( 1, 101 ) )
    
    for number, count in numbers:
        print( 'The number {} has {} 