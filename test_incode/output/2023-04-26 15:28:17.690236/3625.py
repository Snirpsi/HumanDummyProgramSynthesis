#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    while True:
        port = input('Enter a port number: ')
        
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        if port < 1 or port > 65535:
            print('Invalid port number')
            continue
        
        print('Port number %d' % port)
        
        