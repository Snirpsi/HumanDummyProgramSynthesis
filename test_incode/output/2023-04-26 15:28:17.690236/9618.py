#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    numbers = list(range(port))
    
    numbers.remove