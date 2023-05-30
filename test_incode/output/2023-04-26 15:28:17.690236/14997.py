#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and removes fruits. """    
    
    ports = open('/proc/net/tcp', 'r')
    
    while True:
        
        line = ports.readline()
        
        if line == '':
            break
        
        line = line.strip()
        
        if line == '':
            continue
        
        parts = line.split()
        
        if len(parts) < 2:
            continue
        
        ip, port = parts[0], int(parts[1])
        
        if ip == '127.0.0.1':
            continue
        
        try:
            