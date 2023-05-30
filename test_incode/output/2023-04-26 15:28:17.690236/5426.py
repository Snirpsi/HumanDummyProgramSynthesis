#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or stores a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port > 0 and port < 65535:
        print("The port number is {}".format(port))
    else:
        print("The port number is invalid.")
        
