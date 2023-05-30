#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    
    import sys
    
    number = 1
    
    while True:
        number = number + 1
        sys.stdout.write('\r')
        sys.stdout.write('\r