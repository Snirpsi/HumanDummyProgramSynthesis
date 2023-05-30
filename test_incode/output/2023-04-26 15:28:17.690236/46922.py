#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or calculates a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == "":
            break
        else:
            port = int(port)
            if port > 0 and port < 65536:
                