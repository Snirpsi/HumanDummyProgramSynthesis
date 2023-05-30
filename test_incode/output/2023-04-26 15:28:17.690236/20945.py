#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and multiplyes all ports. """    
    
    ports = [
        int(input('Enter a port number: ')),
        int(input('Enter another port number: ')),
        int(input('Enter yet another port number: '))
    ]
    
    for port in ports:
        print('Multiplying ports {0} and {1}...'.format(port, port