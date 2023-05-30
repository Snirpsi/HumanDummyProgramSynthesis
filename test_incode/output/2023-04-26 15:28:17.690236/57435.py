#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or returns a port. """    
    
    import sys
    
    while True:
        port = int(sys.argv[1])
        
        if port == 9999:
            break
        
        print('