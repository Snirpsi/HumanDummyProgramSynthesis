#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and returns all ports. """    
    ports = remove_ports(sys.argv[1])
    for port in ports:
        print(port)
    
