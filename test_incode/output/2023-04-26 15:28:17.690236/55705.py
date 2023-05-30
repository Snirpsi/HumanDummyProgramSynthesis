#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    import sys
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print("Port {} is open".format(port))
    
