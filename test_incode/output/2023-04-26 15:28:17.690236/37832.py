#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or prints all ports. """    
    ports = openPorts()
    for port in ports:
        print(port)
    
