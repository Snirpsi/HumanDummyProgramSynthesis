#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input and iterates over all ports. """    
    ports = input("Enter ports (seperated by comma): ")
    ports = ports.split(',')
    for port in ports:
        print(port)
        