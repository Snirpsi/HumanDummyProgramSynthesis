#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens a port. """    
    while True:
        try:
            port = int(input('Enter a port number: '))
            break
        except ValueError:
            print('Invalid port number')
            
    print('Opening port', port)
    
    