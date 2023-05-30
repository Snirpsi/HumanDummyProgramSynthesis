#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or iterates over user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == "quit":
            break
        else:
            print(port)
            
