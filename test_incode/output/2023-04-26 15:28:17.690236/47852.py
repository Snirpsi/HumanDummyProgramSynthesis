#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or calculates a list of numbers. """    
    ports = [
        port for port in range(1, 65535)
        if port not in 