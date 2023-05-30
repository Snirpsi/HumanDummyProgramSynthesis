#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports or opens user input. """    
    
    ports = input("Enter the ports separated by comma: ").split(",")
    
    for port in ports:
        
        if port == "all":
            
            ports = ports + 