#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports or returns user input. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        port = int(port)
        
        if port == 0 or port == 65535:
            print("Invalid port")
        else:
            print(port)
    
