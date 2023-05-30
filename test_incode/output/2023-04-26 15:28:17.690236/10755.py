#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or iterates over a port. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == 0: break
        print('Enumerating ports from', port)
        
        for port in range(port, 65536):
            print('Port number', port, 'is', port)
            
        print('Bye!')
        
