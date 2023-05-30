#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or converts a list of numbers. """    
    ports = range(10000,20000)
    while True:
        ports = ports + range(10000,20000)
        print(ports)
        time.sleep(1)
