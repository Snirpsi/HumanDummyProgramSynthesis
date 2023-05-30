#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or iterates over numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        print(port * 2)
        
