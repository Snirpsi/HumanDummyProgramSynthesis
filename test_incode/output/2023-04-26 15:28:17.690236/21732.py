#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or prints a port. """    
    port = int(input("Enter a port number: "))
    
    while True:
        print(port)
        port = port + 1
        
