#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and stores words. """    
    
    ports = Ports()
    ports.start()
    
    while True:
        ports.update()
        ports.