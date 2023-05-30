#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or converts a port. """    
    
    port = sys.argv[1]
    
    if port == 'convert':
        convert_port()
    elif port == 'convert