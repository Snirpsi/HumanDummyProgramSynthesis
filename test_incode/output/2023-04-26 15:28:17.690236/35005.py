#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or iterates over all ports. """    
    while True:
        ports = input("Enter ports separated by comma or enter 'quit' to exit: ")
        if ports == 'quit':
            break
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            