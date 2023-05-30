#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and removes a list of numbers. """    
    ports = list(range(1,65535))
    ports.remove(1234)
    print(ports)

<|/ file ext=.py filename=