#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or opens a list of numbers. """    
    while True:
        port = int(input('Enter a port number or enter a number to open a port: '))
        if port == -1:
            break
        
        ports.append(port)
        
        print('Opened port 