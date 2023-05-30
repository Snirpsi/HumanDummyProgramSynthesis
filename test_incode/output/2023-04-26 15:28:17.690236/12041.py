#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or prints user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            