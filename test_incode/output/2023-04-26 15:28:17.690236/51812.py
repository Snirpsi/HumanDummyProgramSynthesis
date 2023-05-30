#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and calculates a port. """    
    
    while True:
        port = input("Enter a port number: ")
        
        if port == "":
            print("Port number cannot be empty")
            continue
        
        if port == "stop":
            break
        
        