#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or stores a port. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port in ports:
            print('Port number {} is already in use'.format(port))
        else:
            ports.append(port)
            print('Port number {} is now in use'.format(port))
    
