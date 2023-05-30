#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or prints user input. """    
    ports = input("Enter the ports separated by comma (no spaces):")
    for port in ports.split(","):
        print(port)
    
