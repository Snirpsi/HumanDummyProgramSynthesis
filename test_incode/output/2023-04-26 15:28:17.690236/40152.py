#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or converts all ports. """    
    
    ports = input("Enter the ports separated by commas: ").split(",")
    
    for port in ports:
        port = int(port)
        
        if port >= 0 and port <= 65535:
            
            