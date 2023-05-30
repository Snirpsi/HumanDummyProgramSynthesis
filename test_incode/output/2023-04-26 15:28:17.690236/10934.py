#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or multiplyes numbers. """    
    while True:
        ports = input("Enter ports: ")
        if ports == 'exit':
            break
        ports = ports.split()
        for port in ports:
            print(port