#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        multiplier = int(input('Enter a multiplier: ')) 
        print('The port multiplied by {} is {}'.format(multiplier, port * multiplier))
        
