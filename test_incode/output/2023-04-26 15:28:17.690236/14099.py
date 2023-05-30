#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or enumerates a port. """    
    
    ports = []
    
    ports.append( ('eth0', 1) )
    ports.append( ('eth1', 2) )
    ports.append( ('eth2', 3) )
    
    for port in ports:
        print(port)
        
