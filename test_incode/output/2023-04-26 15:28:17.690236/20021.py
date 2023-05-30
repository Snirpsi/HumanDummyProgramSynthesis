#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and enumerates all ports. """    
    
    words = []
    
    while True:
        port = input('Enter a port number: ')
        
        if port == '':
            break
        
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        if port not in range(10000, 65535):
            print('Invalid port number')
            continue
        
        words.append(port)
        
        print('Enumerating ports from', port, 'to', port + 1, '...')
        
        for port in range(port, port + 1):
            print('  ', end='')
            
            