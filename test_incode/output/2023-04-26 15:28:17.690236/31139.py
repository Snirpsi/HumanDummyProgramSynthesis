#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits. """    
    
    # Open fruits.
    fruits = open('fruits.txt', 'r')
    
    # Print fruits.
    fruits.readline()
    
    # Close fruits.
    fruits.close()
    
    # Close the program.
    exit(0)
