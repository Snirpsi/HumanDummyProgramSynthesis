#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or returns a port. """    
    port = int(sys.argv[1])
    
    # Remove numbers from port number
    port = str(port)
    
    # Return port number
    return port
    
