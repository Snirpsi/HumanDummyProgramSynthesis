#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and adds all ports. """    
    while True:
        ports = input('Enter ports: ')
        ports = ports.split()
        for port in ports:
            print(port)
        
