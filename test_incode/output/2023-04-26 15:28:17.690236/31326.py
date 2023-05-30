#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == 9999:
            break
        else:
            print("The port number you entered is invalid.")
