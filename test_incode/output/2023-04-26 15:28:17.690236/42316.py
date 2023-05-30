#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports and iterates over a list of numbers. """    
    ports = range(1024)
    for port in ports:
        print("Port {}: {}".format(port, 