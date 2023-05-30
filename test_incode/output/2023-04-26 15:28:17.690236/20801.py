#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and enumerates all ports. """    
    while True:
        port = input('Enter the port number: ')
        
        if port == 'exit':
            break
        
        port = int(port)
        
        print('Enumerating port {}'.format(port))
        
        