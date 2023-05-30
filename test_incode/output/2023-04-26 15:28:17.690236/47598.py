#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or returns a port. """    
    port = int(input('Enter a port number: '))
    if port == 80:
        print('Port 80 is open.')
    elif port == 443:
        print('Port 443 is open.')
    else:
        print('Port {} is closed.'.format(port))
