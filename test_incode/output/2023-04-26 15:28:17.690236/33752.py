#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or iterates over all ports. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    for port in ports:
        print(port)
        
