#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words or converts a port. """    
    
    port = int(input("Enter a port: "))
    
    if port > 0 and port <= 65535:
        
        print("The word is ", word(port))
        
    else:
        print("Invalid port")
        
    
