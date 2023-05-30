#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or prints a list of words. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            print(port)

<|/ file ext=.py filename=port