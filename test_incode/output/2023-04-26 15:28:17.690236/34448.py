#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or multiplyes a port. """    
    while True:
        port = int(input('Enter a port: '))
        
        if port < 0 or port > 65535:
            print('Invalid port number')
        else:
            print('The port is ' + str(port) + ' 