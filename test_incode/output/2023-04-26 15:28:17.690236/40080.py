#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or converts numbers. """    
    ports = [int(x) for x in input().split()]
    ports = ports + list(range(65535, 65536))
    ports = list(set(ports))
    ports.sort()
    for port in ports:
        print("Port ", port, " is open.")
    
