#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or opens a port. """    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        print("Opening port ", port)
        
        