#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 0 and port < 65535:
            port = str(port)
            
            print("The port number is", port)
        else:
            print("Invalid port number")
            
