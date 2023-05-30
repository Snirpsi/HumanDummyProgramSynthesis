#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports. """    
    ports = range(10000, 20000)
    while True:
        for port in ports:
            print("Port 