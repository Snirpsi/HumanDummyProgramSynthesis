#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        print('Port {} is open.'.format(port))
    else:
        print('Usage: python portchecker.py port')
        
