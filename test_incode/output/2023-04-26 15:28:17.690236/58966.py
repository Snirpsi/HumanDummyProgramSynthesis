#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    
    ports = [
        port for port in range(1, 65535)
        if port not in [
            