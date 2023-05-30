#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or enumerates all ports. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number")
        else:
            print("Found port number", port)
            break
    
    
<|/ file ext=.py filename=