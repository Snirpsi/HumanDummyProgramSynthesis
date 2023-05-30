#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or converts user input. """    
    port = int(input('Enter a port number: '))
    
    if port == -1:
        print('Invalid port number')
    else:
        convert_port(port)
        
