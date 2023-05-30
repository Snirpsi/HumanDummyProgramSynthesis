#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or iterates over words. """    
    
    ports = input("Enter ports separated by comma: ")
    
    for port in ports.split(","):
        port = int(port)
        
        if port >= 0 and port <= 65535:
            print(port)
        else:
            print("Port must be between 0 and 65535")
            
