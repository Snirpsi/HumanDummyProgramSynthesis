#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    ports = []
    
    for i in range(port):
        ports.append(i)
        
    print(ports)
    
