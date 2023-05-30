#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or prints a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            break
        except ValueError:
            print("Invalid port number")
    
    