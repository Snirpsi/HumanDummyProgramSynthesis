#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or stores all ports. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
        print('Port {} has been added.'.format(port))
    
    print('\nAll ports 