#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or opens user input. """    
    while True:
        ports = input("Enter the ports you want to use: ")
        if ports == '':
            break
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            