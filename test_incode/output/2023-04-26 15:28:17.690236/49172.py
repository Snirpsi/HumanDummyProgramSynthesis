#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or returns user input. """    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    ports = [int(port) for port in ports]
    
    for port in ports:
        
        if port < 0 or port > 65535:
            print("Invalid port number")
        else:
            print("Port number " + str(port))
    
