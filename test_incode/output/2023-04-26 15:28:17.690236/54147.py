#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or iterates over all ports. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        port = int(port)
        
        if port >= 0 and port < 65535:
            print(port)
        else:
            print("Invalid port")
    
