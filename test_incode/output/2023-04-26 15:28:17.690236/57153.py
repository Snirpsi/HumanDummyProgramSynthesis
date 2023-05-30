#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or converts all ports. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port == -1:
            break
        
        if port > 65535:
            print("Port number too large, exiting...")
            break
        
        if port < 1:
            print("Port number too small, exiting...")
            break
        
        print("Port number 