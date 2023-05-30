#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or iterates over numbers. """    
    
    import sys
    
    # iterate over port
    port = sys.argv[1]
    
    # iterate over numbers
    numbers = sys.argv[2:]
    
    for number in numbers:
        print(number)
        
