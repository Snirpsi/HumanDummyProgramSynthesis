#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or returns user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == 'exit':
            break
        else:
            print('The port number is:', port)
