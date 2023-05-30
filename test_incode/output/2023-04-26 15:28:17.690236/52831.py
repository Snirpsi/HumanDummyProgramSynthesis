#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or returns a port. """    
    port = int(input("Enter a port: "))
    
    if port == -1:
        print("Invalid port")
    else:
        print("The port is " + str(port))
        
