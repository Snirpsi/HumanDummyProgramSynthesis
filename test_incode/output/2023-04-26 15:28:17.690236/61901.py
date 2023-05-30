#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or converts a port. """    
    import sys
    port = int(sys.argv[1])
    
    if port > 65535:
        print('Port number must be less than 65535')
    else:
        print('Port number is', port)
        
