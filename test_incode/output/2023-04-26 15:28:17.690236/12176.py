#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <filename>' % sys.argv[0])
        exit(1)
    
    filename = sys.argv[1]
    
    convert(filename)
    
