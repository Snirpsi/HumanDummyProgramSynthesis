#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or returns numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            print('Bye!')
            break
        else:
            print('The port number is:', port)
            
