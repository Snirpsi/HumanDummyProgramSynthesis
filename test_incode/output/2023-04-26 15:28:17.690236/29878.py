#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or returns user input. """    
    ports = find_ports()
    while True:
        port = input('Enter a port number: ')
        if port in ports:
            print(ports[port])
        else:
            print('Invalid port number')
