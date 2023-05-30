#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or stores a port. """    
    port = int(input("Enter a port: "))
    
    if port > 0 and port <= 65535:
        print("The port is " + str(port))
    else:
        print("The port is invalid")
        
