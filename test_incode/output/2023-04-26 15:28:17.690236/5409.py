#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and returns user input. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        print("The port number is", port)
    
