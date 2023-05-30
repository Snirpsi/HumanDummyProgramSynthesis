#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and iterates over user input. """    
    while True:
        port = int(input("Enter a port number to listen on: "))
        print("Listening on port {}...".format(port))
        
        