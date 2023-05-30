#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and multiplyes a list of numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        numbers = [int(i) for i in input('Enter a list of numbers: ').split()]
        
        print('The port number {} is {}.'.format(port, numbers[0] * numbers[1]))
        
