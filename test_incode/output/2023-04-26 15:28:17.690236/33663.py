#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports. """    
    
    ports = range(65536)
    for port in ports:
        print("Port {} is open".format(port))
    
    
