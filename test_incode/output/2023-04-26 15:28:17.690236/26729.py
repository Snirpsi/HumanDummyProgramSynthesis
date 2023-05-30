#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or stores all ports. """    
    ports = []
    while True:
        ports.append(getPort())
        time.sleep(1)
        
