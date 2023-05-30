#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and converts numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    