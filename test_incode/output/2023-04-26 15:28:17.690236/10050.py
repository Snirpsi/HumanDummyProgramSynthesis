#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits and enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = enumerateFruits(port)
    
    print('\n'.join(map(str, fruits)))
    
