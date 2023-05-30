#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or enumerates words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    ports = list(''.join(