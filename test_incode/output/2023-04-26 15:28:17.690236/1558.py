#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers or opens all ports. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 openports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        openport(port)
    
