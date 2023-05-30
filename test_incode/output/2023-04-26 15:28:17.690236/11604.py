#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and enumerates user input. """    
    port = int(sys.argv[1])
    
    while(True):
        
        port = input("Enter a port number: ")
        
        if port == "":
            print("No port number entered")
        else:
            print("Port number entered")
            
