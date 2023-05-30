#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or stores a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        
        print("Port number 