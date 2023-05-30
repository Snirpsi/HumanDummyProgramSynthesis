#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or converts a port. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        remove_port(8080)
    elif port == 8081:
        remove_port(8081)
    else:
        convert_port(port)
        
