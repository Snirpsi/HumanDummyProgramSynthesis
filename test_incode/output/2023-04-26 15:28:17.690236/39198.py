#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or converts a port. """    
    while True:
        try:
            port = int(input("Enter a port: "))
            break
        except ValueError:
            print("Invalid port. Please try again.")
    
    