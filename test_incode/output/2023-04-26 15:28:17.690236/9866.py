#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or removes all ports. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number")
            continue
        else:
            if port > 0 and port < 65535:
                