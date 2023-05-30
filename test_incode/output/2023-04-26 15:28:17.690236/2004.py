#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and prints a port. """    
    
    port = input("Enter a port number: ")
    
    while True:
        
        print("Port: ", port)
        
        port = input("Enter a port number: ")
        
