#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or returns a port. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("No port number given.")
    else:
        print("The port number is", port)
    
