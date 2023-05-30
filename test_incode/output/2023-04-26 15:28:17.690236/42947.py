#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports or enumerates a list of numbers. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: %s port1 port2 port3" % sys.argv[0])
        exit(1)
    
    ports = [int(x) for x in ports]
    
    ports_removed = ports[:]
    
    for port in ports:
        if port not in ports_removed:
            ports_removed.remove(port)
    
    print("Removed ports: %s" % ports_removed)

<|/ file ext=.py source=github |>