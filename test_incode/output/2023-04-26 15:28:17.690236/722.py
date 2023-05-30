#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        multiplier = int(input("Enter a multiplier: "))
        
        if port == -1:
            break
        
        if port == 0 or port == 65535:
            print("The port number must be between 0 and 65535.")
            continue
        
        if multiplier == 0:
            print("The multiplier must be greater than 0.")
            continue
        
        