#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    ports = enumerate_ports()
    print("\nPorts:")
    for port in ports:
        print("\t", port)
        
