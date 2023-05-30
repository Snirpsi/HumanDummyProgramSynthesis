#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port_str = port.strip()
        
        if port_str == '':
            continue
        
        port = int(port_str)
        
        if port < 0 or port > 65535:
            print("Port %s is invalid." % port_str)
            sys.exit()
        
        convert_port(port)
        
