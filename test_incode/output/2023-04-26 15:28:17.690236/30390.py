#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        port = input('Enter the port you want to listen on: ')
        
        if port == '':
            print('The port you entered is invalid.')
        else:
            print('Listening on port %s...' % port)
            
            