#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or enumerates a port. """    
    port = int(sys.argv[1])
    
    if port == 0: # enumerate all available ports
        ports = range(1024)
    else: # convert all available ports to integers
        ports = [int(port)]
    
    for port in ports:
        webserver.serve_forever()
    
