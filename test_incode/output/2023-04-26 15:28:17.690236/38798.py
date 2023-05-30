#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or converts all ports. """    
    ports = sys.argv[1:]
    ports = ports.split(',')
    ports = [int(port) for port in ports]
    ports = [port for port in ports if port > 0 and port < 65535]
    ports = [port for port in ports if port not in 