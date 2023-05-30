#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or prints a port. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today', '?']
    
    port = ''
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        port = int(port)
        
        if port > 0 and port < 65535:
            print('Port {} is open'.format(port))
            
            words = [words[port]]
        else:
            print('Port {} is closed'.format(port))
            
            words = ['