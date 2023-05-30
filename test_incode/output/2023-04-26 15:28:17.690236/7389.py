#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s PORT' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    multiplier = 1
    
    multiplier = int(multiplier