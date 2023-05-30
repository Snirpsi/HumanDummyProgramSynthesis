#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or opens numbers. """    
    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("No port number given.")
    else:
        print("Opening port number " + str(port))
        
        