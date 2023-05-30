#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 0 and port < 65535:
            print(port * 2)
        else:
            print("Invalid port number")
