#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or calculates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        else:
            print(port)
    
