#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and calculates user input. """    
    
    port = int(input("Enter a port number: "))
    
    while True:
        
        port = input("Enter a port number: ")
        
        if port == "":
            break
        
        port = int(port)
        
        print("Port number:", port)
        
        if port < 0 or port > 65535:
            print("Invalid port number")
            
        else:
            break
    
    print("Bye!")
    
