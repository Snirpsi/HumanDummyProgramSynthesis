#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or multiplyes all ports. """    
    
    ports = input("Enter ports separated by comma: ").split(",")
    
    for port in ports:
        print("Port {} is {}".format(port, 