#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or stores a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == 0:
            break
        
        print("The port number is:", port)
        
        