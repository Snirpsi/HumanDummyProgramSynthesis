#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = int(input('Enter a port: '))
        
        if port == 1000:
            print('Port 1000 is open.')
            break
        else:
            print('Port %d is not open. Try again.' % port)
            
