#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or returns words. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            print('No port number entered')
        else:
            print('Port: ', port)
            
