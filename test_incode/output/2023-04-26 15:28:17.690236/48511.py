#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or removes all ports. """    
    while True:
        ports = input("Enter the ports you want to remove: ").split()
        for port in ports:
            remove_port(port)
