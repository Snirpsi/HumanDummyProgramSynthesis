#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or opens all ports. """    
    
    ports = input("Enter the ports you want to open: ")
    
    for port in ports.split(","):
        
        if port == "all":
            
            ports = input("Enter the ports you want to open: ")
            
            for port in ports.split(","):
                
                port = int(port)
                
                