#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or opens user input. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Please input a port number")
    else:
        print("Opening port 