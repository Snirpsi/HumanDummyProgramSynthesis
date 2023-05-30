#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        remove_port(port)
    else:
        print('Usage: remove_port <port>')
        
