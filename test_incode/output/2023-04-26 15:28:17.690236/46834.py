#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    ports = sys.argv[1:]
    ports = [int(p) for p in ports]
    
    ports = ports[:]
    ports.sort()
    
    for port in ports:
        
        port = str(port)
        
        if port == '0':
            continue
        
        port_