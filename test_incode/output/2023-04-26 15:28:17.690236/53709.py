#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or opens numbers. """    
    while True:
        port = input("Enter a port number: ")
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        
        if port < 0 or port > 65535:
            print("Invalid port number")
            continue
        
        if port == 