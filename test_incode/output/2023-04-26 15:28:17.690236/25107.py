#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and converts a port. """    
    
    ports = input("Enter the ports you want to remove: ")
    ports = ports.split()
    
    for port in ports:
        
        try:
            
            