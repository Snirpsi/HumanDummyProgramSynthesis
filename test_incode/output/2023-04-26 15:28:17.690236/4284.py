#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and stores all ports. """    
    while True:
        ports = input("Enter the ports separated by spaces \n").split()
        for port in ports:
            print(port)
