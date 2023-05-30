#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or converts user input. """    
    while True:
        port = int(input('Enter a port number: '))
        
        if port > 65535:
            print('Port number must be less than 65535')
        elif port < 1:
            print('Port number must be greater than 1')
        else:
            print('Port number is', port)
            
