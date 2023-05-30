#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and returns user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('Invalid port number')
        else:
            print(port)
            
