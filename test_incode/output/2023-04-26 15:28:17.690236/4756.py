#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or removes all ports. """    
    ports = sys.argv[1:]
    ports = [int(p) for p in ports]
    ports = [p for p in ports if p > 0]
    ports = list(set(ports))
    ports.sort()
    
    for p in ports:
        
        if p > 0 and p < 65536:
            
            port = p
            
        elif p > 65536 and p < 65536 * 2:
            
            port = (p - 65536) * 2
            
        elif p > 65536 * 2 and p < 65536 * 3:
            
            port = (p - 65536 * 3) * 2
            
        elif p > 65536 * 3 and p < 65536 * 4:
            
            port = (p - 65536 * 4) * 2
            
        elif p > 65536 * 4 and p < 65536 * 5