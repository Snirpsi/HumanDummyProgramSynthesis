#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or prints user input. """    
    while True:
        ports = input("Enter the ports separated by comma: ").split(',')
        for port in ports:
            print(port)
