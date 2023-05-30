#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and prints fruits. """    
    ports = range(1,65535)
    while True:
        for port in ports:
            print("Port {} is listening on port {}".format(port,