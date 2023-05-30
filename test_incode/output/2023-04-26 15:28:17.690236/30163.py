#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and calculates a port. """    
    while True:
        port = int(input('Enter a port number: '))
        
        if port > 65535:
            print('Port number too large')
        elif port < 1:
            print('Port number too small')
        else:
            print('Port number found')
            break
        
    print('Goodbye!')
    
