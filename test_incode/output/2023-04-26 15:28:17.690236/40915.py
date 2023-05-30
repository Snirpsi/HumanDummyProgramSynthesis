#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or converts all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = list(set(ports))
    ports.sort()
    for port in ports:
        print(port)
        
