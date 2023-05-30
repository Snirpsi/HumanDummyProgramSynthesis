#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input or multiplyes all ports. """    
    
    ports = input("Enter ports: ").split()
    
    for port in ports:
        port = int(port)
        
        if port > 0 and port <= 65535:
            print(port)
        else:
            print("Invalid port")
            
