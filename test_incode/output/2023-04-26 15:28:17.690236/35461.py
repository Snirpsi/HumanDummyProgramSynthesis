#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or converts a port. """    
    
    port = None
    
    try:
        port = int(input("Enter a port number: "))
    except ValueError:
        print("Invalid port number")
        
    if port != None:
        print("The port number is", port)
    else:
        print("No port number given")
        
