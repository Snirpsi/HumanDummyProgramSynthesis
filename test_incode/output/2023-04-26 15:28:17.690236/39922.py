#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input or adds a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port == -1:
        print("Invalid port number")
    else:
        multiply(port)
        
