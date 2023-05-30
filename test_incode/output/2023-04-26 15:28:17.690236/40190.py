#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or returns a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0 or port > 65535:
        print('Invalid port number')
        exit()
    
    ports = enumeratePorts(port)
    
    for port in ports:
        print('Port {0}: {1}'.format(port, ports[port]))
        
    
