#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or prints user input. """    
    while True:
        ports = openports()
        for port in ports:
            print(port)
