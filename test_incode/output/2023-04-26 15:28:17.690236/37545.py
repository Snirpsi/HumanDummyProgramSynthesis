#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or stores a list of numbers. """    
    
    ports = [
        int(input('Enter a port number: ')),
        int(input('Enter another port number: '))
    ]
    
    
    for port in ports:
        print('The port number {} is {}'.format(port, 