#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or iterates over all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <ports>" % sys.argv[0])
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        print("Enumerating port %s" % port)
        
        