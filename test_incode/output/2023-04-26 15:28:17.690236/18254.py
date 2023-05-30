#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and returns a port. """    
    port = 0
    while True:
        port = input("Enter a port number: ")
        try:
            port = int(port)
            break
        except ValueError:
            print("Invalid port number. Try again.")
    
    return port
