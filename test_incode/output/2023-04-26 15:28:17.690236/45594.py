#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or prints a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port < 1 or port > 65535:
        print("Invalid port number")
    else:
        print("Port number {} is open".format(port))
        
