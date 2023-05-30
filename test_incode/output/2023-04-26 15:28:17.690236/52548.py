#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and calculates all ports. """    
    
    ports = []
    
    while True:
        line = input('Enter a port number: ')
        if line == 'q':
            break
        ports.append(int(line))
    
    for port in ports:
        