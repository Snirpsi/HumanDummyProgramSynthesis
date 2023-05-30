#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and opens all ports. """    
    while True:
        ports = openports()
        for port in ports:
            openport(port)
        time.sleep(1)
