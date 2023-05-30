#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words or enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port {} is {}".format(port, ports[port]))
    
