#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or enumerates a list of numbers. """    
    while True:
        try:
            port = int(input('Enter a port number: '))
        except ValueError:
            print('Invalid port number')
            continue
        if port < 0 or port > 65535:
            print('Invalid port number')
            continue
        if port in ports:
            ports.remove(port)
        else:
            print('Port number {} is not in our list'.format(port))
            continue
        print('Port number {} has been removed'.format(port))
