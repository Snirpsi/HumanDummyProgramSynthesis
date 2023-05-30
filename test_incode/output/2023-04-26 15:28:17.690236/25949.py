#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or multiplyes a port. """    
    while True:
        port = input("Enter a port number to multiply or quit: ")
        if port == "quit":
            break
        elif port == "quit\n":
            break
        else:
            print(port * 