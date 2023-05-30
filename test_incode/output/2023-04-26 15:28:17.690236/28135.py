#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or multiplyes numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port > 65535:
            print("Sorry, port number too large.")
        else:
            port = int(port * 65535)
            print("Port number multiplied by 65535: " + str(port))
            
