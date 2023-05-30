#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or prints numbers. """    
    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        
        port = int(port)
        
        if port > 65535:
            print("Port number too large, exiting.")
            break
        
        if port < 1:
            print("Port number too small, exiting.")
            break
        
        print("Port number 