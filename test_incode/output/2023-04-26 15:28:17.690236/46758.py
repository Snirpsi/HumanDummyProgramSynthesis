#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or opens numbers. """    
    ports = sys.argv[1:]
    ports = [int(port) for port in ports]
    ports = list(set(ports))
    ports.sort()
    
    for port in ports:
        openport