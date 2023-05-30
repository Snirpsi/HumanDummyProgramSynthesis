#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or converts a port. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number. Try again.")
        else:
            print("The port number is", port)
            break
