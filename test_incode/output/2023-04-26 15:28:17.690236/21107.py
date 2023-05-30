#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and enumerates all ports. """    
    ports = []
    
    while True:
        ports.append(input('Enter a port number: '))
        
        if ports[-1] == 'done':
            break
        
        print('Enumerating ports from', ports[-1])
        
        for port in range(int(ports[-1]) + 1):
            print('Port #', port, 'is', 