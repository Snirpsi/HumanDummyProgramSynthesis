#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port and iterates over user input. """    
    
    port = int(input("Enter a port number: "))
    
    for port in range(port, 65535):
        print("Port number", port, "is open.")
    
