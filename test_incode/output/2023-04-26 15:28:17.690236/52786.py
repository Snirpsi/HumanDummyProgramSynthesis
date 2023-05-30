#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or iterates over user input. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port in ports:
            print('Port number {} is already in use'.format(port))
        else:
            ports.append(port)
            print('Port number {} is now in use'.format(port))
