#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or prints all ports. """    
    ports = enumerate_ports(sys.argv[1])
    for port in ports:
        print(port)
    
