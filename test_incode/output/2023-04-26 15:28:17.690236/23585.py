#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    
    ports = open('/proc/net/tcp').read().splitlines()
    
    for port in ports:
        if port.find(':') != -1:
            port = int(port.split(':')[1])
            
            