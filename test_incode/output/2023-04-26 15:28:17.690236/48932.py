#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(arg)
    
    for port in ports:
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Port must be between 0 and 65535")
            sys.exit(1)
        
        print("Port %d is open" % port)
        
