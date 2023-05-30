#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port < 1 or port > 65535:
            print("Invalid port number")
        else:
            