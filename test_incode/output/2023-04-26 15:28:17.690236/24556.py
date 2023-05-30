#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or enumerates a list of numbers. """    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    for port in ports:
        print("Port {} is {}".format(port, 