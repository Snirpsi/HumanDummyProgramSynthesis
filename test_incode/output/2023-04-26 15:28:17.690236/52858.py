#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or converts a port. """    
    port = int(input('Enter a port number: '))
    
    if port == -1:
        print('Enter a port number')
    else:
        print('The port number is', port)
        
