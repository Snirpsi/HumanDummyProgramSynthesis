#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or multiplyes a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0:
            word = ''.join(