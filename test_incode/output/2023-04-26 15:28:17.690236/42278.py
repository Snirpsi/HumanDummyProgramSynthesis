#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port or enumerates user input. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number must be between 1 and 65535.")
    else:
        print("Your port number is", port)
        
