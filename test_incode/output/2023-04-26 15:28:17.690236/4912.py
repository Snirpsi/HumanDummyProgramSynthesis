#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    ports = [
        port for port in range(1, 65535)
        if port not in (
            