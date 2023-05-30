#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or adds a port. """    
    while True:
        port = input("Enter a port number: ")
        port = int(port)
        if port > 0 and port < 65535:
            print("Port number ", port, " is available.")
        else:
            print("Port number ", port, " is not available.")
