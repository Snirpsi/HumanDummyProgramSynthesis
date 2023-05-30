#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports. """    
    ports = Ports()
    while True:
        ports.store()
        time.sleep(1)
        
