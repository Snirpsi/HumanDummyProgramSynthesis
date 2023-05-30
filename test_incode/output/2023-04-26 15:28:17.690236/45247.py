#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or calculates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port > 0 and port <= 65535:
            print("Port number entered is " + str(port))
        else:
            print("Port number entered is out of range.")
