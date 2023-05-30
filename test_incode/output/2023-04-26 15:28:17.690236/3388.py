#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and converts words. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    print('\n'.join(ports))
