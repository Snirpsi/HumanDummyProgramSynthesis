#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = input('Enter a port number: ')
        
        if port == '':
            print('No port number entered')
            continue
        
        remove_port(port)
        
