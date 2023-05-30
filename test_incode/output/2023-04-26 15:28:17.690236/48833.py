#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp', 'r')
    for line in ports:
        line = line.strip()
        parts = line.split(':')
        port = parts[0]
        ip = parts[1]
        
        port = int(port)
        
        if port == 8080:
            