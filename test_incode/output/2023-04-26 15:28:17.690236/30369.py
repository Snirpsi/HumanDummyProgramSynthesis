#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp', 'r')
    for line in ports:
        line = line.strip()
        port = int(line)
        
        if port == 80:
            