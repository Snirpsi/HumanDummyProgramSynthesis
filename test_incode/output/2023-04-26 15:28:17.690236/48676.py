#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or stores numbers. """    
    port = int(input("Enter a port number: "))
    
    if port < 0 or port > 65535:
        print("Invalid port number")
    else:
        print("The port number is", port)
        
