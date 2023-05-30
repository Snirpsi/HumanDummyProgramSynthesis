#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or iterates over fruits. """    
    
    import sys
    
    fruit = sys.argv[1]
    
    fruits = list(fruit)
    
    for fruit in fruits:
        print("{} is {}".format(