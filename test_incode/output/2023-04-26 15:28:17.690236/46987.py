#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers and prints a port. """    
    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    