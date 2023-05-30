#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or opens a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port < 1024:
        print("The port is open.")
    else:
        print("The port is closed.")
    
