#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or multiplyes a port. """    
    
    while True:
        port = int(input("Enter a port number: "))
        
        if port < 0 or port > 65535:
            print("Invalid port number")
            continue
        
        if port == 65535:
            print("Port number 65535 is already in use")
            continue
        
        port = int(port * 2)
        
        print("Port number {} is now {}