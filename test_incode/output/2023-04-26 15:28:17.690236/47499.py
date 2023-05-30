#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or calculates user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python word