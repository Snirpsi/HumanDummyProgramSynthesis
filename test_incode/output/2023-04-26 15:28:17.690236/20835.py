#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports. """    
    ports = range(0,65535)
    while True:
        ports = ports + range(65535,65536)
        for port in ports:
            print(port)
        time.sleep(1)
