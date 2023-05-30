#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python word