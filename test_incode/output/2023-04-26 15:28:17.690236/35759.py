#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or prints a list of numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port < 0 or port > 65535:
            print('Invalid port number')
        else:
            print('Port number %d is open.' % port)
            break
        
    print('\nList of open ports:')
    for port in range(1, 65535):
        print('Port number %d is open.' % port)
        
