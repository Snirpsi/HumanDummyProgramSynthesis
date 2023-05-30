#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input or iterates over a port. """    
    
    port = int(input("Enter a port number to connect to: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        
        print("Connecting to port " + str(port))
        
        