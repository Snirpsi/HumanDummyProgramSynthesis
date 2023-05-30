#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    while True:
        ports = range(1,65535)
        ports = [x*y for x,y in zip(ports,ports)]
        print(ports)
        time.sleep(1)
