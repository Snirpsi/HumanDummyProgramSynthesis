#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports or enumerates a list of numbers. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: %s port1 port2 ..." % sys.argv[0])
        sys.exit()
    
    ports = ports.split()
    
    for port in ports:
        
        port = int(port)
        
        if port == -1:
            print("Usage: %s port1 port2 ..." % sys.argv[0])
            sys.exit()
        
        ports.remove(port)
    
    print("Ports removed: %s" % ports)

<|/ file filename=