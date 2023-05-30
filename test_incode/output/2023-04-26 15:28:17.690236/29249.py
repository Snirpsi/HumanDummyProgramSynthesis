#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and iterates over a list of numbers. """    
    
    ports = []
    
    while True:
        ports.append(int(input('Enter a port number: ')))
        
        if ports[-1] == 9999:
            break
        
        ports.pop()
        
    for port in ports:
        
        print('Opening port {}'.format(port))
        
        