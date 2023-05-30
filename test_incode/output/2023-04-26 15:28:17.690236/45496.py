#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or iterates over fruits. """    
    ports = list(fruits.keys())
    ports.sort()
    for port in ports:
        print('serving fruit 