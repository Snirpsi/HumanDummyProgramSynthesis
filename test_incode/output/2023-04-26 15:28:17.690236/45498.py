#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or prints words. """    
    while True:
        ports = input("Enter ports separated by comma: ").split(',')
        for port in ports:
            print(