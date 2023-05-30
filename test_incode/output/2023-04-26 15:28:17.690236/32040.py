#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or removes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 0 and port <= 65535:
            print("Port number " + str(port) + " has been removed")
        else:
            print("Invalid port number")
