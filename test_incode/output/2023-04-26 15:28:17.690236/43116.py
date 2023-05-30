#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or prints numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        number = int(input('Enter a number: '))
        
        if port == 0 or port == 9999:
            print('The port number is invalid.')
        elif port > 9999 or port < 0:
            print('The port number is invalid.')
        else:
            number = port * number
            print('The port number multiplied by {} is {}.'.format(number, number))
            
