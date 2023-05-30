#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [port for port in range(65536)]
    
    for port in ports:
        print(port)
        
