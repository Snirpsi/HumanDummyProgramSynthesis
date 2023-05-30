#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports or prints a list of numbers. """    
    ports = [int(i) for i in input("Enter a list of ports: ").split()]
    ports.sort()
    
    for port in ports:
        if port > 65535:
            print("Port {} is too big!".format(port))
        else:
            print("Port {} is OK!".format(port))
    
