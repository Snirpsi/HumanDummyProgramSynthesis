#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and removes a port. """    
    while True:
        port = input("Enter a port number: ")
        ports.remove(port)
        print("Port removed")
        
