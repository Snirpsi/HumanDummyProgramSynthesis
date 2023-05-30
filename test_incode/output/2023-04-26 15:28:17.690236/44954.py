#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or prints all ports. """    
    
    while True:
        print("\nEnter a port number: ")
        port = int(input("\nEnter a port number: "))
        
        if port > 65535:
            print("\nPort number too large!")
        else:
            print("\nPort number accepted!")
            
