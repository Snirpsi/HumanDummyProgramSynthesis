#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or enumerates all ports. """    
    while True:
        ports = listen_ports()
        if ports:
            print(ports)
        else:
            break
        
