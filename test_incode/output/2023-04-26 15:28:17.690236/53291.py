#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    