#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python word