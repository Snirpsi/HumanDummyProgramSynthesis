#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or returns all ports. """    
    while True:
        ports = input('Enter ports: ')
        if ports == 'exit':
            break
        else:
            ports = ports.split(',')
            for port in ports:
                port = int(port)
                