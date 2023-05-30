#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0 and port <= 65535:
            print('Port %d' % port)
        else:
            print('Port must be between 1 and 65535')
    else:
        print('Usage: %s port' % sys.argv[0])
        
