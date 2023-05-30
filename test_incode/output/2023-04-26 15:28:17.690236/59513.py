#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or prints all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        print(port)
    
