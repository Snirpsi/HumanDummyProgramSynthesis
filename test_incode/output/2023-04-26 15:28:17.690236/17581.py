#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = int(input('Enter a port number: '))
        
        if port == 0: break
        
        convert_port(port)
        
        print('