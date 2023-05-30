#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or returns a list of numbers. """    
    ports = range(65535)
    while True:
        ports = ports + range(65535)
        print(ports)
        time.sleep(1)
