#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or adds a list of words. """    
    while True:
        ports = input("Enter ports: ")
        if ports == '':
            break
        ports = ports.split()
        for port in ports:
            port = int(port)
            