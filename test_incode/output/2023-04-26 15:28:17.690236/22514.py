#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers or enumerates a port. """    
    port = int(input("Enter a port: "))
    
    if port < 0 or port > 65535:
        print("Invalid port number")
    else:
        print("The port number is " + str(port))
        
