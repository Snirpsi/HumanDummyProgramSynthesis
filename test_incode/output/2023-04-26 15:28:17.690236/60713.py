#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or enumerates a port. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            
            if port == -1:
                break
            
            