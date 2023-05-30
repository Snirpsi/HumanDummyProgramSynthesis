#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or opens fruits. """    
    import sys
    port = int(sys.argv[1])
    fruits = open_fruits(port)
    
    for fruit in fruits:
        print(fruit)
    
