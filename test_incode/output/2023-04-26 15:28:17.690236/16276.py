#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or converts all ports. """    
    ports = [int(i) for i in input("Enter ports (separated by space): ").split()]
    
    for port in ports:
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Port {} is invalid.".format(port))
        else:
            print(port)
            
