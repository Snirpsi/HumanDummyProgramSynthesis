#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or calculates all ports. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        
        sys.stdout.write('