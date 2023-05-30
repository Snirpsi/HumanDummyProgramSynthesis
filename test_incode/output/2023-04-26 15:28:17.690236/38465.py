#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or prints user input. """    
    
    port = int(input('Enter a port number: '))
    
    if port > 0 and port <= 65535:
        print('The port number is', port)
    else:
        print('The port number is', port, '