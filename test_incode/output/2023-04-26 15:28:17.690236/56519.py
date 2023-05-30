#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or enumerates a port. """    
    while True:
        port = input('Enter a port number: ')
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        if port < 0 or port > 65535:
            print('Invalid port number')
            continue
        if port in ports:
            ports.remove(port)
        else:
            print('Port number {} is not in ports list'.format(port))
            continue
        print('Port number {} is now in ports list'.format(port))
        print('-'*80)
        
<|/ file ext=.py filename=