#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and enumerates user input. """    
    
    while True:
        port = int(input('Enter a port number: '))
        
        if port > 65535:
            print('Error: port number must be less than 65535.')
        else:
            print('Enumerating ports 1-65535...')
            
            for port in range(1, 65535):
                print('Port {}: {}'.format(port, 