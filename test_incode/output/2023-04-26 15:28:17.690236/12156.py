#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or iterates over a port. """    
    while True:
        port = int(input("Enter a port: "))
        
        if port == -1:
            break
        
        