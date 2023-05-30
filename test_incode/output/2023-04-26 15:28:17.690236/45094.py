#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and multiplyes a list of numbers. """    
    
    port = int(sys.argv[1])
    numbers = [int(x) for x in sys.argv[2:]]
    
    