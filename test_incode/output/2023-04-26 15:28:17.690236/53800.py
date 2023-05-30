#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports and removes numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = [port for port in ports if port > 0]
    ports.sort()
    print(ports)
    
