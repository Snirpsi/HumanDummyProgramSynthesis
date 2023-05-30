#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or converts a port. """    
    
    while True:
        try:
            port = int(input('Enter a port: '))
        except ValueError:
            print('Invalid input. Try again.')
            continue
        
        if port < 0 or port > 65535:
            print('Invalid input. Try again.')
            continue
        
        remove_ports([port])
        
        print('Removed port: {}'.format(port))
        
