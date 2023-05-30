#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        multiplier = int(input("Enter a multiplier: "))
        
        if port == 0 or port > 65535:
            print("Invalid port number")
            continue
        elif multiplier == 0:
            print("Invalid multiplier number")
            continue
        else:
            port = int(port * multiplier)
            print(port)
            
