#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or converts numbers. """    
    while True:
        try:
            port = int(input("Enter a port: "))
        except ValueError:
            print("Invalid port. Try again.")
        else:
            