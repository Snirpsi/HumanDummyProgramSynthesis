#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or converts fruits. """    
    
    ports = []
    
    for port in range(1, 65535):
        
        ports.append(port)
        
    ports.sort()
    
    for port in ports:
        
        print("Port {} is listening on port {}".format(port, 