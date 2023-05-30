#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers and converts a port. """    
    while True:
        number = int(input('Enter a number: '))
        port = int(input('Enter a port: '))
        
        number = number * port
        print('The number is', number, 'and the port is', port)
        
        print('The number is', number, 'and the port is', port, '