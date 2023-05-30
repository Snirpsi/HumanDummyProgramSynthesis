#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and opens all ports. """    
    
    ports = input("Enter the ports you want to open: ")
    
    for port in ports.split(","):
        port = int(port)
        
        openport(port)
        
