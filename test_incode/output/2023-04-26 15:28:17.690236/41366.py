#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or converts a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports = [port * 2 for port in ports]
    ports = list(set(ports))
    ports.sort()
    ports = ports[: