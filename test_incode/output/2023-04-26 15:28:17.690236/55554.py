#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in range(1, 65535):
        
        ports.append(port)
    
    for port in ports:
        
        sys.stdout.write("Port %d is open\n" % port)
    
    sys.stdout.write("Enumerating ports...\n")
    
    for port in ports:
        
        sys.stdout.write("Port %d is %s\n" % (port, 