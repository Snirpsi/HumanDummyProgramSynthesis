#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or converts all ports. """    
    while True:
        ports = input('Enter ports separated by commas:\n').split(',')
        for port in ports:
            print(port)
