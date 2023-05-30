#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or iterates over all ports. """    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'exit':
            break
        
        port = int(port)
        
        print('Converting port {} to {}'.format(port, 