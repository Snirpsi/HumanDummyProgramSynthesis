#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port. """    
    while True:
        port = int(input("Enter a port: "))
        if port > 0 and port <= 65535:
            print("Port {} is open.".format(port))
        else:
            print("Invalid port!")
