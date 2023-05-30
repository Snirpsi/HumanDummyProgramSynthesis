#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or returns a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 65535:
            print("Port number too large. Try again.")
        else:
            break
    print("Port number 