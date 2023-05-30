#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python ports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port > 0:
            ports = ports * port
        else:
            ports = ports / port
    
    print(ports)
    
