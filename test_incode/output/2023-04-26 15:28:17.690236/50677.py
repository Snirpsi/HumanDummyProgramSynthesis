#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and prints fruits. """    
    ports = range(1,65535)
    for port in ports:
        print("Port {} is open on port {}".format(port, 