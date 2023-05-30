#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or adds numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python 