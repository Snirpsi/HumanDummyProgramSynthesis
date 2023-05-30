#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    port = int(input("Enter a port number: "))
    
    while True:
        port *= 10
        print("The port multiplied by 10 is ", port)
        
