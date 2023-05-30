#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or adds all ports. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            print(port)
