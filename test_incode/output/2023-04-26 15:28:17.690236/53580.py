#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and removes a port. """    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number must be less than 65535")
    else:
        print("Port number has been removed")
        
