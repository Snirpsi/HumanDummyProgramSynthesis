#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = input("Enter a port number: ")
        port = int(port)
        
        if port > 65535:
            print("Port number must be less than 65535.")
        else:
            break
        
