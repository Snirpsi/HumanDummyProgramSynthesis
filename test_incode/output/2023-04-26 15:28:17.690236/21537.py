#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = input('Enter a port number: ')
        port = int(port)
        
        if port > 0 and port < 65535:
            print('Port number {} is open'.format(port))
        else:
            print('Port number {} is closed'.format(port))
        
        print('Press ENTER to continue...')
        
        input()
        
        print('Program ends')
        
