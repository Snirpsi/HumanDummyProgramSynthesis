#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or iterates over a list of numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        if port < 0 or port > 65535:
            print("Invalid port number")
        else:
            print(port)
