#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or iterates over all ports. """    
    import sys
    ports = []
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports_iter = iter(ports)
    
    total = 0
    for port in ports_iter:
        total += port
        
    print(total)
    
