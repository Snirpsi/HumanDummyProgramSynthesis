#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or multiplyes user input. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 65535:
        print("Port number must be less than 65535.")
    elif port < 0:
        print("Port number must be greater than 0.")
    else:
        