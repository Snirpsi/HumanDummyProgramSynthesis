#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 convert.py <port>')
        exit()
    
    port = int(sys.argv[1])
    
    port