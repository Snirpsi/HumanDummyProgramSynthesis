#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or prints a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            print(port)
            
