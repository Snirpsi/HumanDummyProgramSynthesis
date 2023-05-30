#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input or enumerates all ports. """    
    
    ports = input("Enter ports separated by comma: ").split(",")
    
    for port in ports:
        
        if port == "all":
            
            ports = input("Enter ports separated by comma: ").split(",")
            
            for port in ports:
                
                