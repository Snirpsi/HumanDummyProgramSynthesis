#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or iterates over a list of numbers. """    
    port = int(sys.argv[1])
    numbers = sys.argv[2:]
    
    for number in numbers:
        