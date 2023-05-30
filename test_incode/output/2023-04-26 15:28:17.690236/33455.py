#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or returns a port. """    
    
    port = None
    
    if sys.argv[1] == 'number':
        port = input('Enter a port number: ')
    elif sys.argv[1] == 'port':
        port = input('Enter a port number: ')
    else:
        print('Invalid argument')
        
    if port is not None:
        
        port = int(port)
        
        print('Opening port {}'.format(port))
        
        open