#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and removes words. """    
    port = int(sys.argv[1])
    
    numbers = range(1,