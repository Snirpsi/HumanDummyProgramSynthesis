#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers and converts all ports. """    
    ports = [
        port for port in range(1, 65535)
        if port not in (