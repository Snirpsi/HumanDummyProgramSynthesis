#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        port = input('Enter a port number: ')
        
        if port == 'exit':
            break
        
        print('Port number:', port)
        
        