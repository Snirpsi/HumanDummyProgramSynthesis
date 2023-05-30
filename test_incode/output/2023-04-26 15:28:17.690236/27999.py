#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or returns all ports. """    
    ports = Ports()
    while True:
        ports.update()
        print(ports.ports)
        time.sleep(1)
        
