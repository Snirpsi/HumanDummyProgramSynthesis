#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = input('Enter a port: ') 
        if port == '':
            break
        
        port = int(port)
        
        print('Converting port {} to {}'.format(port, 