#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers and iterates over all ports. """    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print("Port {0} is {1}".format(port,