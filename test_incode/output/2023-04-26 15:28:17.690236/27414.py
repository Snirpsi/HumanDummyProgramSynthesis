#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or iterates over a port. """    
    port = 0
    
    while True:
        port = input("Enter a port number: ")
        
        if port == '':
            break
        else:
            port = port