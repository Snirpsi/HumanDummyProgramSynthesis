#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers or prints a port. """    
    
    port = int(input('Enter a port number: '))
    
    if port > 65535:
        print('The port number is too large')
    elif port < 0:
        print('The port number is too small')
    else:
        print('The port number is ' + str(port))
