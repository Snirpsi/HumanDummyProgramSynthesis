#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or prints user input. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        
        multiplier = 1
        while multiplier != port:
            multiplier = multiplier * 