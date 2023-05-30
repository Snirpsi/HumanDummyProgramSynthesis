#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or removes a port. """    
    
    port = sys.argv[1]
    
    if port == 'remove':
        remove_port(sys.argv[2])
    else:
        convert_port(port)
    
    
