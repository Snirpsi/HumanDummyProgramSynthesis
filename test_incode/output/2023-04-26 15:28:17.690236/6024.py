#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or opens all ports. """    
    
    ports = input("Enter the ports you want to open: ")
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    
    for port in ports:
        try:
            