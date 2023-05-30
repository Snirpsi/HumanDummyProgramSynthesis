#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and returns numbers. """    
    port = int(sys.argv[1])
    
    ports = [port]
    
    while port:
        port = port - 1
        
        ports.append(port)
    
    return ports
    
