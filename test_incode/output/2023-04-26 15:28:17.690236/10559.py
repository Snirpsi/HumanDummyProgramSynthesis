#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and converts user input. """    
    while True:
        try:
            port = input("Enter a port number: ")
            port = int(port)
            
            