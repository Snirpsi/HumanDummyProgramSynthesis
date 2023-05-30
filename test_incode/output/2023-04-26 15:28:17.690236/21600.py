#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    webserver