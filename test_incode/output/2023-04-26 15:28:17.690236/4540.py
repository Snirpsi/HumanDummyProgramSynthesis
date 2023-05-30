#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and iterates over all ports. """    
    port = int(sys.argv[1])
    
    ports = [port]
    
    while(True):
        ports.append(port + 1)
        
        for port in ports:
            