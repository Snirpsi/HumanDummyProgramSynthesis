#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or converts a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    ports.sort()
    
    ports_str = ""
    
    for port in ports:
        ports_str += str(port) + ", "
    
    ports_str = ports_str[:-2]
    
    print(ports_str)
    
